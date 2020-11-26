from django.db import models

from categories.models import Category
from favorites.models import Favorite


class ProductManager(models.Manager):
    """Respresent a manager responsible of handling product instances."""

    def create_from_openfoodfacts(self, products):
        """Save received product and category data as model instances."""
        for product_info in products:
            # Récupération des catégories et magasins
            categories = product_info.pop("categories")

            # Enregistrement du produit
            product = self.create(**product_info)

            # Création des catégories et association avec le produit
            for category_name in categories:
                category, _ = Category.objects.get_or_create(
                    name=category_name
                )
                product.categories.add(category)

    def find_substitutes(self, product_name, user=None):
        """Recherche des substituts à product_name.

        La stratégie utilisée est de rechercher les produits de meilleur
        nutriscore avec le plus grand nombre de catégories en commun avec
        product_name.

        """
        # On commence par valider le product_name
        if not product_name:  # si égal à None ou une chaine vide
            return None, []
        # Rechercher le produit correspondant à product_name en base
        # de données
        product = (
            self.filter(name__icontains=product_name)
            .order_by('-nutriscore', 'name')
            .first()
        )
        if not product:
            return product, []

        # On élimine de la cherche les produits qui ont déjà été mis en
        # favori par l'utilisateur comme substitut de product.
        products = self.all()
        if user is not None and user.is_authenticated:
            products = products.exclude(
                favorites_as_substitute__in=Favorite.objects.filter(
                    user=user, product=product
                )
            )

        # On retourne une liste de substituts plus sains à product
        substitutes = (
            products.exclude(pk=product.pk)
            .filter(
                categories__in=product.categories.all(),
                nutriscore__lt=product.nutriscore,
            )
            .annotate(num_common_categories=models.Count('pk'))
            .order_by('-num_common_categories', 'nutriscore')
        )
        if substitutes or product.nutriscore > "b":
            return product, list(substitutes)

        # Si aucun produit plus sain n'est trouvé, on recherche des produits
        # de même nutriscore
        return product, list(
            products.exclude(pk=product.pk)
            .filter(
                categories__in=product.categories.all(),
                nutriscore=product.nutriscore,
            )
            .annotate(num_common_categories=models.Count('pk'))
            .order_by('-num_common_categories')
        )

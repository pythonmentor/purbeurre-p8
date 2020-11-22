from django.db import models
from django.conf import settings

from .managers import FavoriteManager


class Favorite(models.Model):
    """Favori enregistré par l'utilisateur pour substituer un produit."""

    substitute = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name="favorites_as_substitute",
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name="favorites_as_product",
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favorites",
    )

    objects = FavoriteManager()

    class Meta:
        verbose_name_plural = 'favorites'
        unique_together = [['substitute', 'product', 'user']]

    def __str__(self):
        return (
            f"{self.user.username}: '{self.product.name}' peut être "
            f"substitué par '{self.substitute.name}'"
        )
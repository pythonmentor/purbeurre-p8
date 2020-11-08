import requests


class OpenfoodfactsClient:
    """Représente une interface à l'API de Openfoodfacts."""

    def __init__(self, lang="fr"):
        """Constructeur du client openfoodfacts.
        Args:
            lang (str): spécifie la langue de l'API à laquelle on souhaite
                accéder. Supporte "en", "fr", "world", la valeur par défaut 
                est "fr".
        Raises:
            ValueError: si lang reçoit une valeur qui n'est pas supportée.
        """
        if lang not in ("fr", "en", "world"):
            raise ValueError('lang supporte les valeurs "fr", "en" et "world"')
        self.url = f"https://{lang}.openfoodfacts.org/cgi/search.pl"

    def get_products_by_popularity(self, page_size=100, number_of_pages=1):
        """Télécharge des produits depuis l'API REST de openfoodfacts par
        ordre de popularité.
        Args:
            page_size (int): nombre de produits à télécharger par page. Les
                valeurs supportées sont 20, 50, 100, 250, 500, 1000. La valeur 
                par défaut est 100.
            number_of_pages (int): nombre de pages à télécharger. La valeur
                par défaut est 1.
        Return:
            Une liste de dictionnaires décrivant les produits de openfoodfacts
            téléchargés. Si une erreur réseau intervient, la liste retournée
            est vide.
        Raises:
            ValueError si page_size n'est pas une valeur supportée.
        """
        if page_size not in (20, 50, 100, 250, 500, 1000):
            raise ValueError(
                "page_size doit avoir une valeur de "
                "20, 50, 100, 250, 500 ou 1000"
            )
        products = []
        for page in range(1, number_of_pages+1):
            params = {
                "action": "process",
                "json": True,
                "sort_by": "unique_scans_n", # popularité
                "page_size": page_size,
                "page": page
            }
            try:
                response = requests.get(self.url, params=params)
                response.raise_for_status()
            except requests.RequestException:
                return [] # En cas d'erreur, on retourne une liste vide

            data = response.json().get("products")
            if data is not None:
                products.extend(data)
            
        return products
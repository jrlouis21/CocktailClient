import requests


class CocktailDBClient:
    def __init__(self, api_key):
        self.session = requests.Session()
        self.session.params = {"api_key": api_key}
        self.base_url = "https://www.thecocktaildb.com/api/json/v1/1"

    def _get(self, endpoint, params=None):
        response = self.session.get(f"{self.base_url}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()

    def search_cocktail_by_name(self, name):
        return self._get("search.php", params={"s": name})

    def list_cocktails_by_first_letter(self, letter):
        return self._get("search.php", params={"f": letter})

    def search_ingredient_by_name(self, name):
        return self._get("search.php", params={"i": name})

    def lookup_cocktail_by_id(self, cocktail_id):
        return self._get("lookup.php", params={"i": cocktail_id})

    def lookup_ingredient_by_id(self, ingredient_id):
        return self._get("lookup.php", params={"iid": ingredient_id})

    def lookup_random_cocktail(self):
        return self._get("random.php")

    def filter_by_ingredient(self, *ingredients):
        params = {"i": ",".join(ingredients)}
        return self._get("filter.php", params=params)

    def filter_by_alcoholic(self, alcoholic):
        return self._get("filter.php", params={"a": alcoholic})

    def filter_by_category(self, category):
        return self._get("filter.php", params={"c": category})

    def filter_by_glass(self, glass):
        return self._get("filter.php", params={"g": glass})

    def list_categories(self):
        return self._get("list.php", params={"c": "list"})["drinks"]

    def list_glasses(self):
        return self._get("list.php", params={"g": "list"})["drinks"]

    def list_ingredients(self):
        return self._get("list.php", params={"i": "list"})["drinks"]

    def list_alcoholic_filters(self):
        return self._get("list.php", params={"a": "list"})["drinks"]

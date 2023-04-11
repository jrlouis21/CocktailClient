import httpx


class CocktailDBClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.thecocktaildb.com/api/json/v1"

        self.client = httpx.Client()

    def __del__(self):
        self.client.close()

    def _get(self, endpoint):
        response = self.client.get(f"{self.base_url}/{self.api_key}/{endpoint}")
        response.raise_for_status()
        return response.json()

    def search_cocktail_by_name(self, name):
        endpoint = f"search.php?s={name}"
        return self._get(endpoint)

    def list_cocktails_by_first_letter(self, letter):
        endpoint = f"search.php?f={letter}"
        return self._get(endpoint)

    def search_ingredient_by_name(self, name):
        endpoint = f"search.php?i={name}"
        return self._get(endpoint)

    def lookup_cocktail_by_id(self, id):
        endpoint = f"lookup.php?i={id}"
        return self._get(endpoint)

    def lookup_ingredient_by_id(self, id):
        endpoint = f"lookup.php?iid={id}"
        return self._get(endpoint)

    def lookup_random_cocktail(self):
        endpoint = "random.php"
        return self._get(endpoint)

    def filter_by_ingredient(self, ingredient):
        endpoint = f"filter.php?i={ingredient}"
        return self._get(endpoint)

    def filter_by_alcoholic(self, alcoholic):
        endpoint = f"filter.php?a={alcoholic}"
        return self._get(endpoint)

    def filter_by_category(self, category):
        endpoint = f"filter.php?c={category}"
        return self._get(endpoint)

    def filter_by_glass(self, glass):
        endpoint = f"filter.php?g={glass}"
        return self._get(endpoint)

    def list_categories(self):
        endpoint = "list.php?c=list"
        return self._get(endpoint)

    def list_glasses(self):
        endpoint = "list.php?g=list"
        return self._get(endpoint)

    def list_ingredients(self):
        endpoint = "list.php?i=list"
        return self._get(endpoint)

    def list_alcoholic_filters(self):
        endpoint = "list.php?a=list"
        return self._get(endpoint)


if __name__ == "__main__":
    client = CocktailDBClient(api_key="1")
    print(client.list_categories())

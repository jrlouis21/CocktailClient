import json
from urllib.parse import urlparse

from uplink import Consumer, Path, Query, get
from uplink import json as jsontype
from uplink import returns
from uplink.decorators import response_handler


@returns.json(key="drinks")
@jsontype
@get
def get_json_key():
    """
    Template for GET request that consumes and produces JSON nested in a key.
    """


def log_response_info(response):
    """Response Handler to print response attributes"""
    print(
        f"""
        URL: {response.url}
        Method: {response.request.method}
        HTTP Code: {response.status_code}
        Reason: {response.reason}
        JSON: {response.request.body}
        Response: {json.loads(response.content)}
        """
    )

    return response


def parse_drink(drink):
    response = {}
    response["id"] = drink.get("idDrink")
    response["url"] = "https://www.thecocktaildb.com/drink/" + response["id"]
    response["name"] = drink.get("strDrink")
    response["alt_name"] = drink.get("strDrinkAlternate")
    response["category"] = drink.get("strCategory", "Cocktail")
    response["is_alchoholic"] = (
        True if drink.get("strAlcoholic") == "Alcoholic" else False
    )
    response["glass_type"] = drink.get("strGlass", "Cocktail Glass")
    response["instructions"] = drink.get("strInstructions", "Instructions unknown.")

    response["ingredients"] = []
    for i in range(1, 15):
        ingredient = drink.get("strIngredient" + str(i), "")
        if ingredient:
            measurement = drink.get("strMeasure" + str(i), "")
            response["ingredients"].append((measurement, ingredient))
        else:
            break

    return response


class CocktailClient(Consumer):
    """A Python Client for `TheCocktailDB` API"""

    def __init__(self, base_url, token):
        base_url = urlparse(base_url)

        base_url = f"{base_url.scheme}://{base_url.netloc}/api/json/v1/{token}/"

        super(CocktailClient, self).__init__(base_url=base_url)

    #####################
    ## PRIVATE METHODS ##
    #####################

    # @response_handler(log_response_info)
    @get_json_key("random.php")
    def __get_random_cocktail(self):
        """Get a Random Cocktail"""

    # @response_handler(log_response_info)
    @get_json_key("lookup.php")
    def get_cocktail(self, i: Query = None):
        """Get a specific cocktail by ID"""

    @get_json_key("lookup.php?{search_type}={search_param}")
    def __search_cocktail(self, search_type, search_param):
        """Search for cocktails"""

    ####################
    ## PUBLIC METHODS ##
    ####################

    def random(self):
        drink = self.__get_random_cocktail()
        return parse_drink(drink[0])


if __name__ == "__main__":
    client = CocktailClient(base_url="https://thecocktaildb.com/", token="1")
    print(client.get_cocktail(i=12442))

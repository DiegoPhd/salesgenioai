########## ONLY FOR LOCAL CONFIGURATION ##########

import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_a_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(folder_a_directory)

##################################################

from pytest_bdd import scenarios, then, when, parsers
from screenpy import (
    AnActor,
    ContainsTheText,
    IsEmpty,
    IsGreaterThan,
    IsGreaterThanOrEqualTo,
    IsNot,
    ReadExactly,
    See,
    SeeAllOf,
    noted_under,
)

from actions.reads_the_catalog import ReadTheCatalog
from data.catalog_model import Product
from utils.note_constants import OUT_OF_STOCK_PRODUCTS, PRODUCTS, SEARCH_PRODUCT_REPONSE
from actions.save_out_of_stock_products import SaveTheOutOfStockProducts
from questions.the_available_products_text import (
    TheAvailableProductsText,
)
from actions.search_the_product import SearchThe


scenarios("../features/purchase_assistant.feature")


@when("Diego loads the catalog.json file")
def diego_loads_the_catalog_json_file(Diego: AnActor) -> None:
    Diego.attempts_to(ReadTheCatalog())


@when("Diego asks about the available products")
def diego_asks_about_the_available_products(Diego: AnActor) -> None:
    Diego.attempts_to(ReadTheCatalog(), SaveTheOutOfStockProducts())


@when(parsers.parse("Diego asks about {product_to_search} information"))
def diego_asks_about_product_information(
    Diego: AnActor, product_to_search: str
) -> None:
    Diego.attempts_to(ReadTheCatalog(), SearchThe.product(product_to_search))


@then("the catalog loads correctly and the products can be iterated over without error")
def the_catalog_loads_correctly_and_the_products_can_be_iterated_over_without_error(
    Diego: AnActor,
) -> None:
    products: list[Product] = noted_under(PRODUCTS)
    for i in products:
        Diego.should(
            SeeAllOf(
                (i.PRODUCT_ID, IsNot(IsEmpty())),
                (
                    i.Name,
                    IsNot(IsEmpty()),
                ),
                (
                    i.Description,
                    IsNot(IsEmpty()),
                ),
                (
                    i.Price,
                    IsGreaterThan(0),
                ),
                (
                    i.Stock_availabiility,
                    IsGreaterThanOrEqualTo(0),
                ),
            )
        )


@then("Diego should only see the available products")
def diego_should_only_see_the_available_products(
    Diego: AnActor,
) -> None:
    out_of_stock_products: list[str] = noted_under(OUT_OF_STOCK_PRODUCTS)
    the_available_product_text: str = TheAvailableProductsText().answered_by(Diego)

    for i in out_of_stock_products:
        Diego.should(See(the_available_product_text, IsNot(ContainsTheText(i))))


@then("Diego should see the product information")
def diego_should_see_the_product_information(
    Diego: AnActor,
) -> None:
    product_to_search_response: tuple[str, str] = noted_under(SEARCH_PRODUCT_REPONSE)
    product_info: str = product_to_search_response[0]

    Diego.should(
        SeeAllOf(
            (product_info, ContainsTheText("The product is")),
            (
                product_info,
                ContainsTheText("with description"),
            ),
            (
                product_info,
                ContainsTheText("and price:"),
            ),
        )
    )


@then("Diego should see that the product does not exist")
def Diego_should_see_that_the_product_does_not_exist(
    Diego: AnActor,
) -> None:
    product_to_search_response: tuple[str, str] = noted_under(SEARCH_PRODUCT_REPONSE)
    product_info: str = product_to_search_response[0]

    Diego.should(See(product_info, ReadExactly("Product not found.")))


@then("Diego should see the stock availability")
def diego_should_only_see_the_stock_availability(
    Diego: AnActor,
) -> None:
    product_to_search_response: tuple[str, str] = noted_under(SEARCH_PRODUCT_REPONSE)
    product_stock_info: str = product_to_search_response[1]
    Diego.should(
        SeeAllOf(
            (product_stock_info, ContainsTheText("The product")),
            (
                product_stock_info,
                ContainsTheText("is in stock with availability:"),
            ),
        )
    )


@then("Diego should see that the product is out of stock")
def diego_should_see_that_the_product_is_out_of_stock(
    Diego: AnActor,
) -> None:
    product_to_search_response: tuple[str, str] = noted_under(SEARCH_PRODUCT_REPONSE)
    product_stock_info: str = product_to_search_response[1]

    Diego.should(See(product_stock_info, ReadExactly("Product not found.")))

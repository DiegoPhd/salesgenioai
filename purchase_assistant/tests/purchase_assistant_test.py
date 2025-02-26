########## ONLY FOR LOCAL CONFIGURATION ##########

import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_a_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(folder_a_directory)

##################################################

from pytest_bdd import scenarios, then, when
from screenpy import (
    AnActor,
    IsEmpty,
    IsGreaterThan,
    IsGreaterThanOrEqualTo,
    IsNot,
    SeeAllOf,
    noted_under,
)

from actions.reads_the_catalog import ReadTheCatalog
from data.catalog_model import Product
from utils.note_constants import PRODUCTS


scenarios("../features/purchase_assistant.feature")


@when("Diego loads the catalog.json file")
def diego_loads_the_catalog_json_file(Diego: AnActor) -> None:
    Diego.attempts_to(ReadTheCatalog())


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

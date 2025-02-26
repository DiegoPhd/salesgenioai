########## ONLY FOR LOCAL CONFIGURATION ##########
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_a_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(folder_a_directory)

##################################################

from screenpy import Actor, beat, noted_under
from data.catalog_model import Product
from utils.note_constants import PRODUCTS

AVAILABLE_PRODUCTS_TEXT = "The available products are: "


class TheAvailableProductsText:

    @beat("{} asks about the available products")
    def answered_by(self, _: Actor) -> str:
        products: list[Product] = noted_under(PRODUCTS)
        available_products: list[str] = [
            item.Name for item in products if item.Stock_availabiility > 0
        ]
        available_products_text: str = AVAILABLE_PRODUCTS_TEXT
        for i in available_products:
            available_products_text += f"{i}, "

        return available_products_text

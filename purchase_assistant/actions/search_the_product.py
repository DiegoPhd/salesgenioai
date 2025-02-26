########## ONLY FOR LOCAL CONFIGURATION ##########
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_a_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(folder_a_directory)

##################################################

from typing_extensions import Self
from screenpy import Actor, MakeNote, beat, noted_under
from data.catalog_model import Product
from utils.note_constants import PRODUCTS, SEARCH_PRODUCT_REPONSE

AVAILABLE_PRODUCT_TEXT = "The product {name} is in stock with availability: {stock}."
NON_EXISTENT_PRODUCT = "Product not found."


class SearchThe:

    def __init__(self, product_name: str) -> None:
        self.product_name = product_name

    @classmethod
    def product(cls, product_name: str) -> Self:
        return cls(product_name)

    @beat("{} asks about the available of {product_name}")
    def perform_as(self, the_actor: Actor) -> None:
        products: list[Product] = noted_under(PRODUCTS)
        the_actor.attempts_to(
            MakeNote.of(NON_EXISTENT_PRODUCT).as_(SEARCH_PRODUCT_REPONSE)
        )
        for item in products:
            if (
                item.Name.lower() == self.product_name.lower()
                and item.Stock_availabiility > 0
            ):
                response: str = AVAILABLE_PRODUCT_TEXT.format(
                    name=item.Name, stock=item.Stock_availabiility
                )
                the_actor.attempts_to(MakeNote.of(response).as_(SEARCH_PRODUCT_REPONSE))

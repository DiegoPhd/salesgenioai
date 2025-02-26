########## ONLY FOR LOCAL CONFIGURATION ##########

import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_a_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(folder_a_directory)

##################################################

from screenpy import Actor, MakeNote, beat, noted_under
from data.catalog_model import Product
from utils.note_constants import OUT_OF_STOCK_PRODUCTS, PRODUCTS


class SaveTheOutOfStockProducts:

    @beat("{} saves the out of stocks products")
    def perform_as(self, the_actor: Actor) -> None:
        products: list[Product] = noted_under(PRODUCTS)

        out_of_stock_products: list[str] = [
            item.Name for item in products if item.Stock_availabiility == 0
        ]

        the_actor.attempts_to(
            MakeNote.of(out_of_stock_products).as_(OUT_OF_STOCK_PRODUCTS)
        )

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
PRODUCT_INFORMATION_TEXT = (
    "The product is {name} with description: {description} and price: {price}."
)


class SearchThe:

    def __init__(self, product_name: str) -> None:
        self.product_name = product_name

    @classmethod
    def product(cls, product_name: str) -> Self:
        return cls(product_name)

    @beat("{} asks about the available of {product_name}")
    def perform_as(self, the_actor: Actor) -> None:
        products: list[Product] = noted_under(PRODUCTS)

        product_info: str = NON_EXISTENT_PRODUCT
        product_stock: str = NON_EXISTENT_PRODUCT
        response: tuple[str, str] = (product_info, product_stock)

        the_actor.attempts_to(MakeNote.of(response).as_(SEARCH_PRODUCT_REPONSE))
        for item in products:
            if self.exist_the_product(item):
                product_info = PRODUCT_INFORMATION_TEXT.format(
                    name=item.Name, description=item.Description, price=item.Price
                )
                if self.there_stock_available(item):
                    product_stock = AVAILABLE_PRODUCT_TEXT.format(
                        name=item.Name, stock=item.Stock_availabiility
                    )

                response = (product_info, product_stock)
                the_actor.attempts_to(MakeNote.of(response).as_(SEARCH_PRODUCT_REPONSE))

    def exist_the_product(self, item: Product) -> bool:
        return bool(item.Name.lower() == self.product_name.lower())

    def there_stock_available(self, item: Product) -> bool:
        return bool(item.Stock_availabiility > 0)

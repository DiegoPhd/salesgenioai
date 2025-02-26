########## ONLY FOR LOCAL CONFIGURATION ##########

import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
folder_a_directory = os.path.abspath(os.path.join(current_directory, os.pardir))
sys.path.append(folder_a_directory)

##################################################

import json
from screenpy import Actor, MakeNote, beat
from data.catalog_model import Product
from utils.note_constants import PRODUCTS


class ReadTheCatalog:

    @beat("{} reads the catalog")
    def perform_as(self, the_actor: Actor) -> None:
        with open("purchase_assistant/resources/catalog.json") as file:
            catalog = json.load(file)

        products = [Product(**item) for item in catalog]

        the_actor.attempts_to(MakeNote.of(products).as_(PRODUCTS))

from shop.helper.type_hint import Basket, Product
from shop.helper.const import exit_commands
from shop.utils.funcs import (
    clear_screen,
    search_basket,
)


def handle_search_command(basket: Basket):
    clear_screen()
    keyword: str = input('Search >> ')
    if keyword in exit_commands:
        return None
    search_basket(basket, keyword)

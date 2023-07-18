from shop.helper.type_hint import Basket
from shop.utils.funcs import (
    clear_screen,
    show_basket
)


def handle_show_command(basket: Basket):
    clear_screen()
    show_basket(basket)

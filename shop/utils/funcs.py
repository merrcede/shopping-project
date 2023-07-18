import os
import logging
from difflib import SequenceMatcher
from typing import List, Dict

from shop.models.product import products
from shop.helper.type_hint import Basket, Product
from shop.helper.const import exit_commands

logger = logging.getLogger(__name__)


def similarity(actual: str, expected: str) -> float:
    """
       Calculate the similarity ratio between two strings.

       Args:
           actual (str): The actual string.
           expected (str): The expected string.

       Returns:
           float: The similarity ratio between the two strings.
       """
    return SequenceMatcher(None, actual, expected).ratio()


def search_basket(basket: List[Dict[str, any]], keyword: str):
    """
      Search for products in the basket based on a keyword and display the results.

      Args:
          basket (List[Dict[str, any]]): The list of products in the basket, where each product is represented as a dictionary.
          keyword (str): The keyword to search for in the product colors.

      Returns:
          None
      """
    print(f"Search for {keyword}...")
    results = [
        (product, similarity(product['color'], keyword))
        for product in basket
        if keyword.lower() in product['color'].lower()
    ]
    if results:
        print(f'Found ({len(results)}) results:')
        for product, score in results:
            print(
                f"ID: {product['id']},"
                f" Color: {product['color']},"
                f" Price: {product['price']},"
                f" Discount: {product['discount']}")
    else:
        print("No result found.")


def add_item(basket: List[Dict], item: Dict) -> List[Dict]:
    """
    Add an item to the basket.

    Args:
        basket (List[Dict]): The list representing the basket.
        item (Dict): The item to be added to the basket.

    Returns:
        List[Dict]: The updated basket with the item added.
    """
    logger.debug(f"Adding `{item}` to user's basket.")
    basket.append(item)
    return basket


def remove_item(basket: Basket, item_id: int) -> bool:
    """
       Remove an item from the basket based on the provided item ID.

       Args:
           basket (List[Dict[str, Any]]): The basket containing the items.
           item_id (int): The ID of the item to remove.

       Returns:
           bool: True if the item is successfully removed, False otherwise.
       """
    logger.debug(f"Removing item with ID: {item_id} from the basket.")
    for item in basket:
        if item['id'] == item_id:
            basket.remove(item)
        logger.info('Item removed from the basket.')
        return True

    logger.warning('Item not found in the basket.')
    return False


def show_basket(basket: Basket) -> None:
    """
    Display the contents of the basket.

    Args:
        basket (Basket): The basket containing the items.

    Returns:
        None
    """
    print("Your Basket:")
    for product in basket:
        print(f"- ID: {product['id']}, "
              f"Color: {product['color']}, "
              f" Price: {product['price']}, "
              f"Discount: {product['discount']}")
    try:
        total_price = calculate_total_price(basket)
        print(f"Total Amount: {total_price}")
    except ValueError as e:
        print(f"Error calculating total amount: {str(e)}")


def show_total_items(basket: Basket) -> None:
    """
    Display the total number of items in the basket.

    Args:
        basket (Basket): The basket containing the items.

    Returns:
        None
    """
    print(f'You have {len(basket)} items in the basket.')


def is_valid_item(item: Product, products: list[dict], raise_exc=False) -> bool | Exception:
    """
       Validates whether the given item is valid based on the available products.

       Args:
           item (dict): The item (product) to validate.
           products (List[dict]): The list of available products to check against.
           raise_exc (bool, optional): A flag indicating whether to raise an exception when the item is invalid.
                                       Defaults to False.

       Returns:
           Union[bool, None]: Returns True if the item is valid, False if it is invalid and raise_exc is False,
                              or None if it is invalid and raise_exc is True.

       Raises:
           Exception: If raise_exc is True and the item is invalid, an exception is raised with a descriptive message.
        """
    if not item:
        is_valid = False
        message = 'Product must not be empty.'
    elif item not in products:
        is_valid = False
        message = 'Product must be one of the available products.'
    else:
        is_valid = True

    if raise_exc and not is_valid:
        raise Exception(message)
    else:
        return is_valid


def show_help():
    """
    Displays the available commands and their descriptions.

    Usage:
        show_help()

    Returns:
        None

    """
    logger.info('----')
    logger.info("Please enter a command when you see `>`.")
    logger.info("Please write `add` to enter your product.")
    logger.info("Please write `show` to show your products in the basket.")
    logger.info("Please write `help` to show the available commands.")
    logger.info("Please write `exit` to exit the program.")
    logger.info('----')


def show_error(error: Exception) -> None:
    """
    Displays the given error message.

    Args:
        error (Exception): The error message to be displayed.

    Returns:
        None
    """
    print(f"Error: {error}")


def calculate_total_price(basket: Basket) -> float:
    """
    Calculate the total price of the products in the basket, including tax.

    Args:
        basket (Basket): The basket containing the products.

    Returns:
        float: The total price of the products including tax.
    """
    try:
        tax_rate = 0.1  # Assuming 10% tax rate
        total_price = 0.0

        for product in basket:
            price = product.get('price', 0)
            discount = product.get('discount', 0)
            if discount is None:
                discount = 0
            discounted_price = price - (price * discount / 100)
            total_price += discounted_price

        tax_amount = total_price * tax_rate
        total_price_with_tax = total_price + tax_amount

        logging.info(f"Total price calculation successful. Total price with tax: {total_price_with_tax}")
        return total_price_with_tax

    except Exception as e:
        logging.error(f"Error calculating total price: {str(e)}")
        raise


def clear_screen():
    os.system("clear")

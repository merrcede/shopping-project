from shop.helper.type_hint import Basket, Product


def remove_command(basket: Basket) -> None:
    print("Your Basket:")
    for product in basket:
        print(f"- ID: {product['id']}, "
              f"Color: {product['color']}, "
              f"Price: {product['price']}, "
              f"Discount: {product['discount']}")

    try:
        product_id = int(input('Enter the ID of the product you want to remove: '))
    except ValueError:
        print("Invalid input. Please enter a valid integer for the product ID.")
        return

    removed = False
    for i, product in enumerate(basket):
        if product['id'] == product_id:
            del basket[i]
            print('Product removed from the basket.')
            removed = True
            break

    if not removed:
        print('Product not found in the basket.')

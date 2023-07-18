# Galaxy_sport shop
import logging
from conf import *
from shop.models.product import genders, categories, brands, sizes, products

basket = []

print("Welcome to your shop =)", "\n")

try:
    while True:
        print('Choose your gender:')
        for gender_item in genders:
            print(gender_item['id'], '-', gender_item['title'])
        gender = int(input('Your choice:'))

        print('Choose your category:')
        for category_item in categories:
            print(category_item['id'], '-', category_item['title'])
        category = int(input("Your choice:"))

        print('Choose your brand:')
        for brand_item in brands:
            print(brand_item['id'], '-', brand_item['title'])
        brand = int(input('Your choice:'))

        print('Choose your size:')
        for size_item in sizes:
            print(size_item['id'], '-', size_item['title'])
        size = int(input('Your choice:'))

        matching_products = []
        for product in products:
            if gender in product['gender_id'] and \
                    category in product['categories_id'] and \
                    brand in product['brands_id'] and \
                    size in product['sizes_id']:
                matching_products.append(product)

        if matching_products:
            for product in matching_products:
                print(f"ID: {product['id']}, "
                      f"Color: {product['color']}, "
                      f"Price: {product['price']}, "
                      f"Discount: {product['discount']}")
            product_id = int(input('Enter product ID that you want to add to basket: '))
            for product in matching_products:
                if product_id == product['id']:
                    basket.append(product)
            print('Product added to basket.')
            buy_more = input('Do you want to buy more? (yes/no): ')
            if buy_more.lower() != 'yes':
                break

        else:
            print('No product found.')

except ValueError:
    logging.error('Invalid input entered.')
    print('Invalid input. Please enter a valid choice.')

except Exception as e:
    logging.exception('An error occurred: ' + str(e))
    print('An error occurred. Please try again later.')









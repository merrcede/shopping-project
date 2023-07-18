import logging

logging.basicConfig(
    filename='shop.log',
    level=logging.DEBUG,
    format='%(name)s - %(levelname)s - %(message)s',
    filemode='a'
)
logging.basicConfig(filename='shop.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')
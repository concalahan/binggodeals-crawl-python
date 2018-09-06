class Product:
    name = ''
    category = ''
    store_name = ''
    description = ''
    price = set()

    def __init__(self, name, category, store_name, description, price):
        Product.name = name
        Product.category = category
        Product.store_name = store_name
        Product.description = description
        Product.price = price
        # self.boot()

    # Creates directory and files for project on first run and starts the spider
    # def boot():
""" """


import requests
from mes_aliments.models import Category, Product, Favorite

class Psql_data:
    """ """

    def __init__(self):
        """init the class"""
        self.category_name = ['Pizza', 'boisson', 
                              'dessert', 'salade', "cookie"]
        self.url = "https://fr.openfoodfacts.org/cgi/search.pl?"
        self.product_categorie = []
        self.input_data = 0
        self.insert_category_name()
        #self.get_data_openfoodfacts()
        #self.insert_product_data()

    def insert_category_name(self):
        """Save the Category's name in the database"""
        if Category.objects.count() != 5:
            for name in self.category_name:
                self.input_data = Category(name=name)
                print(self.input_data)
                self.input_data.save()

    def get_data_openfoodfacts(self):
        """Get data from the API of OpenFoodFacts"""
        for value in self.category_name:
            self.payload = {"search_terms": value,
                            "json": 1,
                            "action": "process",
                            "lang": "fr",
                            "page_size": "100",
                            "page": "1"
                            }
            # Request to the API
            self.json_request = requests.get(self.url, params=self.payload,)
            # Export data as json data
            self.json_category = self.json_request.json()
            # Add all json data in a list to make easier the usage
            self.product_categorie.append(self.json_category)
        self.category = Category.objects.all()
        print(self.category[0])
    def insert_product_data(self):
        """Insert and Save the data of each product in the database"""
        if Product.objects.count() != 500:
            for i in range(len(self.category_name)):
                print(i)
                for product in self.product_categorie[i]['products']:
                    self.name = product.get('product_name')
                    self.brands = product.get('brands'),
                    self.nutriscore_grade = product.get('nutriscore_grade'),
                    self.url = product.get('url'),
                    self.stores = product.get('stores')
                    self.input_data_product = Product(
                        name=self.name,
                        brands=self.brands,
                        nutriscore_grade=self.nutriscore_grade,
                        url=self.url,
                        stores=self.stores,
                        category=i)
                    self.input_data_product.save()

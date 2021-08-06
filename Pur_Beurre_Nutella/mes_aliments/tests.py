'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from .models import Category, Contact, Product, Favorite
from .helper.function import substitute_search, product_search


class ModelsTestCase(TestCase):
    '''Models test class'''
    def setUp(self):
        '''Init the test with creation of one category and one product'''
        self.category_name = ['pizza', 'boisson']
        self.pizza_name = ['pizza1', 'pizza2', 'pizza3']
        self.pizza_nutriscore = ['c', 'b', 'd']
        for name in self.category_name:
            self.category = Category.objects.create(name=name)
        for name, nutriscore in zip(self.pizza_name, self.pizza_nutriscore):
            self.pizza = Product.objects.create(
                name=name, brands='marque', nutriscore_grade=nutriscore,
                url='url', image='image', stores='magasin', category_id=1)
        self.boisson1 = Product.objects.create(
            name='boisson1', brands='marque', nutriscore_grade='b',
            url='url', image='image', stores='magasin', category_id=2)
        self.result = "pizza1"

    def test_product_search(self):
        '''Test the product_search method if returns the correct value'''
        self.my_product = product_search('pizza1')[0]
        self.assertEqual(self.my_product.name, self.result)

    def test_substitute_search(self):
        self.substitutes = substitute_search('pizza3')
        print(self.substitutes)


class IndexPageTestCase(TestCase):
    '''Index page test class'''
    def test_index_page_returns_200(self):
        '''Test if the Http request returns 200'''
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


"""class ProductPageTestCase(TestCase):
    '''Product page test class'''
    def setUp(self):
        '''Init all needed data for the test
           In that case, create new products is necessary'''
        self.category_name = ['pizza', 'boisson']
        self.pizza_name = ['pizza1', 'pizza2', 'pizza3']
        self.pizza_nutriscore = ['c', 'b', 'd']
        for name in self.category_name:
            self.category = Category.objects.create(name=name)
        for name, nutriscore in zip(self.pizza_name, self.pizza_nutriscore):
            self.pizza = Product.objects.create(
                name=name, brands='marque', nutriscore_grade=nutriscore,
                url='url', image='image', stores='magasin', category_id=1)
        self.boisson1 = Product.objects.create(
            name='boisson1', brands='marque', nutriscore_grade='b',
            url='url', image='image', stores='magasin', category_id=2)

    def test_product_page_returns_200(self, *args):
        '''Test if the Http request returns 200
           and all substitute with a best nutriscore
           for the selected product '''
        response = self.client.post('/mes_substituts/')
        self.assertEqual(response.status_code, 200)"""


class LoginPageTestCase(TestCase):
    '''Login page test class'''
    def test_login_page_returns_200(self):
        '''Test of the Http request returns 200'''
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        '''Init all needed data to test the user's login'''
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        '''Test if the user is logged after the login step'''
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)


class AccountPageTestCase(TestCase):
    '''Account page test class'''
    def setUp(self):
        '''Init all needed data for the test'''
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        '''Test if the Http request returns 200 when the user is logged'''
        # send login data
        self.client.post('/login/', self.credentials, follow=True)
        response = self.client.get('/mon_compte/')
        self.assertEqual(response.status_code, 200)

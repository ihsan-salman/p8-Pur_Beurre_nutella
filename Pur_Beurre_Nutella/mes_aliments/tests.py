'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


from django.urls import reverse
from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User

from .models import Category, Contact, Product, Favorite

#Create your tests here

class IndexPageTestCase(TestCase):
    '''Index page test class'''
    def test_index_page_returns_200(self):
        '''Test if the Http request returns 200'''
        response  = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

class ProductPageTestCase(TestCase):
    '''Product page test class'''
    def setUp(self):
        '''Init all needed data for the test
           In that case, create new products is necessary'''
        pizza = Category.objects.create(name="pizza")
        boisson = Category.objects.create(name="boisson")
    def test_product_page_returns_200(self):
        '''Test if the Http request returns 200
           and all substitute with a best nutriscore
           for the selected product '''
        pass


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

'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User

from .models import Category, Contact, Product, Favorite

#Create your tests here

class IndexPageTestCase(TestCase):
   def test_index_page(self):
      response  = self.client.get(reverse('home'))
      self.assertEqual(response.status_code, 200)

'''class ProductPageTestCase(TestCase):
   def test_product_page_returns_200(self):
      pizza = Category.objects.create(name="pizza")'''

class AccountPageTestCase(TestCase):
   def test_account_page_returns_200(self):
      response = self.client.get(reverse('mon_compte'))
      self.assertEqual(response.status_code, 200)


class LoginPageTestCase(TestCase):
    def test_login_page_returns_200(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)
      

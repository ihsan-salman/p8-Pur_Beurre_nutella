'''!/usr/bin/python3
   -*- coding: Utf-8 -'''


from django.urls import reverse
from django.test import TestCase

from .models import Category, Contact, Product, Favorite

#Create your tests here

class IndexPageTestCase(TestCase):
   def test_index_page(self):
      response  = self.client.get(reverse('home'))
      self.assertEqual(response.status_code, 200)

class ProductPageTestCase(TestCase):
   def test_product_page_returns_200(self):

from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=200, unique=True, default='DEFAULT VALUE')

	def __str__(self):
		return self.name

class Product(models.Model):
	name = models.CharField(max_length=200, unique=True)
	brands = models.CharField(max_length=200)
	nutriscore_grade = models.CharField(max_length=1)
	url = models.URLField()
	stores = models.CharField(max_length=200)
	category = models.ForeignKey(Category, on_delete=models.PROTECT)
	def __str__(self):
		return self.name

class Favorite(models.Model):
	product = models.OneToOneField(Product, 
		on_delete=models.PROTECT,
		related_name='product')
	substitute = models.OneToOneField(Product, 
		on_delete=models.PROTECT,
		related_name='substitute')

	def __str__(self):
		return self.product
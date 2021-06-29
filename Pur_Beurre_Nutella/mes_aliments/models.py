from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True, default='DEFAULT VALUE')

    def __str__(self):
        return self.name

class Contact(models.Model):
    email = models.EmailField(max_length=100)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=100)


class Product(models.Model):
	name = models.CharField(max_length=400, unique=False)
	brands = models.CharField(max_length=400)
	nutriscore_grade = models.CharField(max_length=10)
	url = models.URLField()
	image = models.URLField()
	stores = models.CharField(max_length=400, null=True)
	category = models.ForeignKey(Category, on_delete=models.PROTECT, default='DEFAULT VALUE')

	
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
from django.db import models
from Products.choices import animal, category

class Product (models.Model):
    name_product = models.CharField(max_length=50, verbose_name= 'Nombre del producto')
    price = models.IntegerField(verbose_name='Precio')
    stock = models.BooleanField(verbose_name='Stock')
    animal = models.CharField(max_length=12, choices=animal, verbose_name='Animal')
    category = models.CharField(max_length=50, choices=category, verbose_name="Categoria")

    def __str__(self):
        return self.name_product


from django.db import models
from Users.models import User
from Products.models import Product

class Order (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name= 'Nombre de usuario')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name= 'Producto')


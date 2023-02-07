from django.db import models

class User (models.Model):
    name = models.CharField(max_length=80, verbose_name= 'Nombre')
    address = models.CharField(max_length=50, verbose_name= 'Dirección')
    phone_number = models.IntegerField(verbose_name= 'Telefono')
    
    def __str__(self):
        return self.name
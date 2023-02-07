from django import forms
from Products.choices import animal, category

class ProducForm (forms.Form):
    name_product = forms.CharField(max_length=50, label= 'Nombre del producto')
    price = forms.IntegerField(label= 'Precio')
    stock = forms.BooleanField(label= 'Stock')
    animal = forms.ChoiceField(choices=animal, label='Animal')
    category = forms.ChoiceField(choices=category, label= 'Categoria')
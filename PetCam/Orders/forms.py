from django import forms

class OrderForm (forms.Form):
    user = forms.CharField(label= 'Usuario')
    product = forms.CharField(label= 'Producto')

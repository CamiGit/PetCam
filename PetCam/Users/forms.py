from django import forms

class UserForm (forms.Form):
    name = forms.CharField(max_length=80, label= 'Nombre')
    address = forms.CharField(max_length=50, label= 'Dirección')
    phone_number = forms.IntegerField(label= 'Numero Telefonico')
    
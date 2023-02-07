from django import forms

class CategoryForm (forms.Form):
    name_category = forms.CharField(max_length=50, label='Nombre de la categoria')

    
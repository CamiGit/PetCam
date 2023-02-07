from django.contrib import admin
from Products.models import Product

#admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_product', 'price', 'stock', 'animal', 'category',)
    list_filter = ('stock',)
    search_fields = ('animal', 'category', 'name_product')


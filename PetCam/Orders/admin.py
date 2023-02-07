from django.contrib import admin
from Orders.models import Order

# admin.site.register(Order)

@admin.register(Order)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    search_fields = ('user',)
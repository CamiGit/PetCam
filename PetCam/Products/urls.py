from django.urls import path

from Products.views import new_product, list_product, update_product, productDeleteView, productDetailView

urlpatterns = [
    path('new_product/', new_product),
    path('list_product/', list_product),
    path('update_product/<int:pk>/', update_product),
    path('delete_product/<int:pk>/', productDeleteView.as_view()),
    path('detail_product/<int:pk>/', productDetailView.as_view()),
]
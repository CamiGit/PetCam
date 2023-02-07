from django.urls import path
from Orders.views import OrdersListView, OrdersCreateView, OrdersDeleteView, OrdersUpdateView

urlpatterns = [
    path('new_order/', OrdersCreateView.as_view()),
    path('list_order/', OrdersListView.as_view()),
    path('delete_order/<int:pk>/', OrdersDeleteView.as_view()),
    path('update_order/<int:pk>/',  OrdersUpdateView.as_view()),

]
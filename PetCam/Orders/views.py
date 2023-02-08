from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from Orders.models import Order


class OrdersListView(ListView):
    model = Order
    template_name = 'Orders/list_orders.html'

class OrdersCreateView(CreateView):
    model = Order
    template_name = 'Orders/new_orders.html'
    fields = '__all__'
    success_url = '/Orders/list_order/'

class OrdersUpdateView(UpdateView):
    model = Order
    template_name = 'Orders/update_orders.html'
    fields = '__all__'
    success_url = '/Orders/list_order/'

class OrdersDeleteView(DeleteView):
    model = Order
    template_name = 'Orders/delete_orders.html'
    success_url = '/Orders/list_order/'
from django.shortcuts import render
from django.views.generic import DeleteView, DetailView

from Products.models import Product
from Products.forms import ProducForm

def new_product(request):
        if request.method == 'GET':
            context = {
                'form' : ProducForm
            }
            return render(request, 'Products/new_products.html', context=context)
        
        elif request.method == 'POST':
            form = ProducForm(request.POST)
            if form.is_valid():
                Product.objects.create(
                    name_product = form.cleaned_data['name_product'],
                    price = form.cleaned_data['price'],
                    stock = form.cleaned_data['stock'],
                    animal = form.cleaned_data['animal'],
                    category = form.cleaned_data['category']
                )
                context = {
                    'message' : 'Producto Creado'
                }
                return render(request, 'Products/new_products.html', context=context)
            else:
                context = {
                    'form_errors' : form.errors,
                    'form' : ProducForm
                }
                return render(request, 'Products/new_products.html', context=context)

def list_product(request):
    if 'search' in request.GET:
        search = request.GET['search']
        Product_all = Product.objects.filter(name_product__icontains = search)
    else:    
        Product_all = Product.objects.all()
    context = {
        'products' : Product_all
        }
    return render(request, 'Products/list_products.html', context=context)
    
def update_product(request, pk):
    
    product = Product.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form' : ProducForm(
                initial={
                    'name_product': product.name_product,
                    'price': product.price,
                    'stock': product.stock,
                    'animal': product.animal,
                    'category': product.category,
                }
            )
        }
        return render(request, 'Products/update_products.html', context=context)

    elif request.method == 'POST':
        form = ProducForm(request.POST)
        if form.is_valid():
            product.name_product = form.cleaned_data['name_product']
            product.price = form.cleaned_data['price']
            product.stock = form.cleaned_data['stock']
            product.animal = form.cleaned_data['animal']
            product.category = form.cleaned_data['category']
            product.save()
            context = {
                'message' : 'Producto Actualizado'
            }
            return render(request, 'Products/update_products.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form' : ProducForm
            }
            return render(request, 'Products/update_products.html', context=context)

class productDeleteView(DeleteView):
    model = Product
    template_name = 'Products/delete_products.html'
    success_url = '/Products/list_product/'

class productDetailView(DetailView):
    model = Product
    template_name = 'Products/detail_products.html'




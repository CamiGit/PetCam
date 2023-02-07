from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView

from Categories.models import Category
from Categories.forms import CategoryForm

def new_category(request):
    
    if request.method == 'GET':
        context = {
            'form' : CategoryForm
        }
        return render(request, 'Categories/new_categories.html', context=context)

    elif request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            Category.objects.create(name_category = form.cleaned_data['name_category'])
            context = {
                'message' : 'Categoria Creada'
            }
            return render(request, 'Categories/new_categories.html', context=context)
        else:
            context = {
                'form_errors': form.errors,
                'form' : CategoryForm
            }
            return render(request, 'Categories/new_categories.html', context=context)
    

def list_category(request):
    if 'search' in request.GET:
        search = request.GET['search']
        Category_all = Category.objects.filter(name_category__icontains = search)
    else:
        Category_all =  Category.objects.all()
    context = {
        'Category': Category_all
    }
    return render(request, 'Categories/list_categories.html', context=context)


class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'Categories/update_categories.html'
    fields = '__all__'
    success_url = '/Categories/list_category/'

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'Categories/delete_Categories.html'
    success_url = '/Categories/list_category/'

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from Users.models import User
from Users.forms import UserForm


def new_user(request):
    if request.method == 'GET':
        context = {
            'form' : UserForm
        }
        return render(request, 'Users/new_users.html', context=context)

    elif request.method == 'POST':
        form = UserForm(request.POST)
        if  form.is_valid():
            User.objects.create(
                name = form.cleaned_data['name'],
                address = form.cleaned_data['address'],
                phone_number = form.cleaned_data['phone_number']
            )
            context = {
                'message' : 'Usuario Creado'
            }
            return render(request, 'Users/new_users.html', context=context)
        else:
            context = {
                'form_errors' : form.errors,
                'form' : UserForm
            }
            return render(request, 'Users/new_users.html', context=context)

@login_required
def list_user(request):
    if 'search' in request.GET:
        search = request.GET['search']
        User_all = User.objects.filter(name__icontains = search)
    else:    
        User_all = User.objects.all()
    context = {
        'user' : User_all
    }
    return render(request, 'Users/list_users.html', context=context)
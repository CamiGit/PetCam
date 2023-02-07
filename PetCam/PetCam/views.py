from django.shortcuts import render

def index(request):
    return render(request, 'Categories/list_categories.html', context={})
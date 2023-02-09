from django.urls import path

from Categories.views import new_category, list_category, CategoryUpdateView, CategoryDeleteView, About_me

urlpatterns = [
    path('new_category/', new_category),
    path('list_category/', list_category, name='category'),
    path('update_category/<int:pk>/', CategoryUpdateView.as_view()),
    path('delete_category/<int:pk>/', CategoryDeleteView.as_view()),
    path('about_me/', About_me)
]
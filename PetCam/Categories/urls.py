from django.urls import path

from Categories.views import new_category, list_category, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path('new_category/', new_category),
    path('list_category/', list_category),
    path('update_category/<int:pk>/', CategoryUpdateView.as_view()),
    path('delete_category/<int:pk>/', CategoryDeleteView.as_view()),
]
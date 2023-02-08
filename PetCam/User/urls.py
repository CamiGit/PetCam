from django.urls import path

from User.views import login_view, registrer
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login_view/', login_view, name='login'),
    path('logout_view/', LogoutView.as_view(template_name = 'User/logout.html')),
    path('signup_view/', registrer)
]
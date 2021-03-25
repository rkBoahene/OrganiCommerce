from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


app_name = 'users'
urlpatterns = [
    # url('login/', views.user_login, name='login'),
    url('login/', auth_views.LoginView.as_view(), name='login'),
    url('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # url('', product_list, name='dashboard'),
    url('register/', views.register, name='register')
]

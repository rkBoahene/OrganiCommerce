from django.conf.urls import include, url

from . import views

app_name = 'users'
urlpatterns = [
    url('accounts/', include('django.contrib.auth.urls')),
    url('dashboard/', views.dashboard, name='dashboard'),
    url('register/', views.register, name='register')
]

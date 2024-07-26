# gestiondeusuario/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='gestionusuario/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', views.profile, name='profile'),  
    path('grupo/', views.grupo, name='grupo'),  
    path('crearart/', views.crearart, name='crearart'),  
    path('crearart2/', views.crearart2, name='crearart2'),  
    path('crearart3/', views.crearart3, name='crearart3'), 
    path('crearart4/', views.crearart4, name='crearart4'),  
    path('crearart5/', views.crearart5, name='crearart5'),  
    path('', views.index, name='index'),  
]
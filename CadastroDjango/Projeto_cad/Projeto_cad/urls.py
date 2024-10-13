from django.urls import path
from app_Projeto_cad import views

urlpatterns = [
    path('',views.home,name='home'),

    path('usuarios/',views.usuarios,name='list_users')
]

from django.urls import path
from . import views

# DEFINA O APP_NAME AQUI
app_name = 'produtos'

urlpatterns = [
    path('', views.produto_list, name='produto_list'),
    path('<int:pk>/', views.produto_detail, name='produto_detail'),
]
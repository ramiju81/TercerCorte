from django.urls import path
from . import views

urlpatterns = [
    path('crear_pedidos/', views.crear_pedidos, name='crear_pedidos'),
    path('listar_pedidos/', views.listar_pedidos, name='listar_pedidos'),
]

#http://localhost:8000/pedidos/crear_pedidos/
#http://localhost:8000/pedidos/listar_pedidos/

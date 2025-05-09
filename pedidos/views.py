from django.shortcuts import render

# Create your views here.

def crear_pedidos(request):
    return render(request, 'pedidos/crear_pedido.html')

def listar_pedidos(request):
    return render(request, 'pedidos/lista_pedidos.html')
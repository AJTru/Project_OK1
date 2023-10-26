from django.shortcuts import render
from cursos.models import articulos
from django.http import HttpRequest
# Create your views here.

def catalogo(request):
    arts = articulos.objects.all()
    return render(request, "catalogo.html", {"arts":arts})

def single_product(request, id):
    # arts = articulos.objects.all()
    product = articulos.objects.get(pk=id)
    # product_name = product.cantidad
    # print(product_name)
    return render(request, "single-product.html", {"product":product})
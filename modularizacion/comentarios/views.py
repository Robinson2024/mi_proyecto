from django.shortcuts import render
from django.http import HttpResponse
from .models import Comentario  # Importamos el modelo Comentario la tabla de la base de datos

def test(request):
    return HttpResponse('funciona correctamente')

def create(request):
    # comentario = Comentario(nombre='Robin', score=5, email='robin@example.com', contenido='este es un contenido')
    # comentario.save()
    Comentario.objects.create(nombre='Robin', score=5, email='robin@example.com', contenido='este es un contenido')
    return HttpResponse('Ruta para probar la creacion de modelos')

def delete(request):
    #comentario = Comentario.objects.get(id=19)
    #comentario.delete()
    Comentario.objects.filter(id=18).delete()
    return HttpResponse('Ruta para probar la eliminacion de modelos')
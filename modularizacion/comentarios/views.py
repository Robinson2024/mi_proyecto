from django.shortcuts import render
from django.http import HttpResponse
from .models import Comentario # Importamos el modelo Comentario la tabla de la base de datos

def test(request):
    return HttpResponse('funciona correctamente')

def create(request):
    comentario = Comentario(nombre='Juan', score=5, email='juan@example.com', contenido='este es un contenido')
    comentario.save()
    return HttpResponse(f'Comentario guardado con ID: {comentario.id}')
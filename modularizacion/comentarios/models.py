from django.db import models

# Create your models here.
class Comentario(models.Model):
    nombre = models.CharField(max_length=255, null=False)
    score = models.IntegerField(default=3)
    email = models.EmailField()
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)
    
    

    def __str__(self):
        return self.nombre
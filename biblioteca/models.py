from django.db import models
from django.utils import timezone
from django.contrib import admin

class Libro(models.Model):
    isbn = models.IntegerField(max_length=13)
    titulo = models.CharField(max_length=50)
    #para agregar imagen se tiene que intalar Pillow y luego hacer la referencia en settings.py
    #portada = models.ImageField(upload_to='photos/')
    autor = models.CharField(max_length=25)
    editorial = models.CharField(max_length=30)
    pais = models.CharField(max_length=20)
    anio = models.IntegerField(max_length=5)
    
    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    dpi = models.CharField(max_length=25)
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre
    
class Prestamo(models.Model):
    usuario = models.ForeignKey(Usuario)
    libro = models.ManyToManyField(Libro)
    fecha_prestamo = models.DateTimeField(blank=True, null=True)
    fecha_propuesta = models.DateField()
    fecha_devolucion = models.DateTimeField(blank=True, null=True)
    
    def prestar(self):
        self.fecha_prestamo = timezone.now()
        self.save()

    
class PrestamoInLine(admin.TabularInline):
    model = Prestamo
    extra = 1
    
class PrestamoAdmin(admin.ModelAdmin):
    inlines = (PrestamoInLine,)
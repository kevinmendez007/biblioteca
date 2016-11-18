from django.shortcuts import render
from .models import Libro

def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'biblioteca/libro_list.html', {'libros':libros})

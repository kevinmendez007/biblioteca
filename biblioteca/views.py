from django.shortcuts import render
from .models import Libro
from .forms import PrestamoForm

def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'biblioteca/libro_list.html', {'libros':libros})

def prestamo_new(request):
    if request.method == "POST":
        form = PrestamoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = PrestamoForm()
    return render(request, 'biblioteca/prestamo_edit.html', {'form': form})
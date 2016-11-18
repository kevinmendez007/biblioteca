from django.shortcuts import render

def libro_list(request):
    return render(request, 'biblioteca/libro_list.html', {})

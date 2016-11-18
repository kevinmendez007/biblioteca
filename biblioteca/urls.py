from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.libro_list),
    url(r'^prestamo/new/$', views.prestamo_new, name='prestamo_new'),
]
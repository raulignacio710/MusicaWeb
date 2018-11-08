from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r"^nosotros/$", views.nosotros, name = "nosotros"),
    url(r"^contacto/$", views.contacto, name = "contacto"),
    url(r"^login/$", views.ingresar, name = "login"),
    url(r"^gestionClientes/$", views.gestionClientes, name = "gestionClientes"),
    url(r"^gestionClientes/actualizar/(?P<pk>[0-9_]+)$", views.actualizarCliente, name = "actualizarCliente"),
    url(r"^gestionClientes/eliminar/(?P<pk>[0-9_]+)$", views.eliminarCliente, name = "eliminarCliente"),
    url(r"^gestionInstrumentos/$", views.gestionInstrumentos, name = "gestionInstrumentos"),
    url(r"^gestionInstrumentos/actualizar/(?P<pk>[0-9_]+)$", views.actualizarInstrumento, name = "actualizarInstrumento"),
    url(r"^gestionInstrumentos/eliminar/(?P<pk>[0-9_]+)$", views.eliminarInstrumento, name = "eliminarInstrumento"),
    url(r"", views.index, name="index"),
]

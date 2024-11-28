from django.urls import path
from cliente_app import views

urlpatterns = [
    path('', views.inicio_vista, name='inicio_vista'),  # Vista principal que muestra los clientes
    path('registrarCliente/', views.registrarCliente, name='registrarCliente'),  # Ruta para registrar nuevo cliente
    path('seleccionarCliente/<id_cliente>', views.seleccionarCliente, name='seleccionarCliente'),  # Ver detalles del cliente
    path('editarCliente/', views.editarCliente, name='editarCliente'),  # Editar un cliente
    path('borrarCliente/<id_cliente>', views.borrarCliente, name='borrarCliente'),  # Eliminar cliente
]

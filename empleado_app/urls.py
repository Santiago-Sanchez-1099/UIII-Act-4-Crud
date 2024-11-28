from django.urls import path
from empleado_app import views

urlpatterns = [
    path('', views.inicio_vista, name='inicio_vista'),  # Vista principal que muestra los empleados
    path('registrarEmpleado/', views.registrarEmpleado, name='registrarEmpleado'),  # Ruta para registrar nuevo empleado
    path('seleccionarEmpleado/<id_empleado>', views.seleccionarEmpleado, name='seleccionarEmpleado'),  # Ver detalles del empleado
    path('editarEmpleado/', views.editarEmpleado, name='editarEmpleado'),  # Editar un empleado
    path('borrarEmpleado/<id_empleado>', views.borrarEmpleado, name='borrarEmpleado'),  # Eliminar empleado
]

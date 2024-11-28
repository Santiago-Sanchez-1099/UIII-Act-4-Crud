from django.shortcuts import render, redirect
from .models import Empleado

# Mostrar la lista de empleados
def inicio_vista(request):
    losempleados = Empleado.objects.all()
    return render(request, 'gestionarEmpleado.html', {'misempleados': losempleados})

# Registrar un nuevo empleado
def registrarEmpleado(request):
    id_empleado = request.POST["num_id_empleado"]
    nombres = request.POST["txt_nombres"]
    apellidos = request.POST["txt_apellidos"]
    email = request.POST["txt_email"]
    password = request.POST["txt_password"]
    puesto = request.POST["txt_puesto"]
    fecha_registro = request.POST["date_fecha_registro"]

    # Crear el nuevo empleado
    Empleado.objects.create(
        id_empleado=id_empleado,
        nombres=nombres,
        apellidos=apellidos,
        email=email,
        password=password,  # Asegúrate de encriptar la contraseña si es necesario
        puesto=puesto,
        fecha_registro=fecha_registro,
    )
    return redirect('/')

# Seleccionar un empleado para editar
def seleccionarEmpleado(request, id_empleado):
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    return render(request, "editarEmpleado.html", {"misempleados": empleado})

# Editar un empleado existente
def editarEmpleado(request):
    id_empleado = request.POST["num_id_empleado"]
    nombres = request.POST["txt_nombres"]
    apellidos = request.POST["txt_apellidos"]
    email = request.POST["txt_email"]
    password = request.POST["txt_password"]
    puesto = request.POST["txt_puesto"]
    fecha_registro = request.POST["date_fecha_registro"]

    # Buscar y actualizar el empleado
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.nombres = nombres
    empleado.apellidos = apellidos
    empleado.email = email
    empleado.password = password  # Encripta si es necesario
    empleado.puesto = puesto
    empleado.fecha_registro = fecha_registro
    empleado.save()

    return redirect('/')

# Borrar un empleado
def borrarEmpleado(request, id_empleado):
    empleado = Empleado.objects.get(id_empleado=id_empleado)
    empleado.delete()
    return redirect("/")

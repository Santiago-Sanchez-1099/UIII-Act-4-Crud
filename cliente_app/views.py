from django.shortcuts import render, redirect
from .models import Cliente

# Mostrar la lista de clientes
def inicio_vista(request):
    losclientes = Cliente.objects.all()
    return render(request, 'gestionarCliente.html', {'misclientes': losclientes})

# Registrar un nuevo cliente
def registrarCliente(request):
    id_cliente = request.POST["num_id_cliente"]
    nombres = request.POST["txt_nombres"]
    apellidos = request.POST["txt_apellidos"]
    email = request.POST["txt_email"]
    password = request.POST["txt_password"]
    telefono = request.POST["txt_telefono"]
    direccion = request.POST["txt_direccion"]

    # Crear el nuevo cliente
    Cliente.objects.create(
        id_cliente=id_cliente,
        nombres=nombres,
        apellidos=apellidos,
        email=email,
        password=password,  # Asegúrate de encriptar la contraseña si es necesario
        telefono=telefono,
        direccion=direccion,
    )
    return redirect('/')

# Seleccionar un cliente para editar
def seleccionarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    return render(request, "editarCliente.html", {"misclientes": cliente})

# Editar un cliente existente
def editarCliente(request):
    id_cliente = request.POST["num_id_cliente"]
    nombres = request.POST["txt_nombres"]
    apellidos = request.POST["txt_apellidos"]
    email = request.POST["txt_email"]
    password = request.POST["txt_password"]
    telefono = request.POST["txt_telefono"]
    direccion = request.POST["txt_direccion"]

    # Buscar y actualizar el cliente
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.nombres = nombres
    cliente.apellidos = apellidos
    cliente.email = email
    cliente.password = password  # Encripta si es necesario
    cliente.telefono = telefono
    cliente.direccion = direccion
    cliente.save()

    return redirect('/')

# Borrar un cliente
def borrarCliente(request, id_cliente):
    cliente = Cliente.objects.get(id_cliente=id_cliente)
    cliente.delete()
    return redirect("/")

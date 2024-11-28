from django.shortcuts import render, redirect
from .models import Venta
# Create your views here.

def inicio_vista(request):
    lasventas=Venta.objects.all()
    return render(request, 'gestionarVenta.html',{'misventas':lasventas})

def registrarVenta(request):
    id_venta = request.POST["num_id_venta"]
    fecha_venta = request.POST["date_fecha_venta"]
    producto = request.POST["txt_producto"]
    cantidad = request.POST["num_cantidad"]
    total = request.POST["num_total"]
    metodo_pago = request.POST["txt_metodo_pago"]
    id_producto = request.POST["num_id_producto"]
    id_empleado = request.POST["num_id_empleado"]
    id_cliente = request.POST["num_id_cliente"]


    guardarventa = Venta.objects.create(id_venta=id_venta,fecha_venta=fecha_venta,producto=producto,cantidad=cantidad,
    total=total,metodo_pago=metodo_pago,id_producto=id_producto,id_empleado=id_empleado,id_cliente=id_cliente)
    return redirect('/')

def seleccionarVenta(request, id_venta):
    venta=Venta.objects.get(id_venta=id_venta)
    return render(request, "editarVenta.html",{"misventas":venta})

def editarVenta(request):
    id_venta = request.POST["num_id_venta"]
    fecha_venta = request.POST["date_fecha_venta"]
    producto = request.POST["txt_producto"]
    cantidad = request.POST["num_cantidad"]
    total = request.POST["num_total"]
    metodo_pago = request.POST["txt_metodo_pago"]
    id_producto = request.POST["num_id_producto"]
    id_empleado = request.POST["num_id_empleado"]
    id_cliente = request.POST["num_id_cliente"]
    venta=Venta.objects.get(id_venta=id_venta)
    venta.fecha_venta=fecha_venta
    venta.producto=producto
    venta.cantidad=cantidad
    venta.total=total
    venta.metodo_pago=metodo_pago
    venta.id_producto=id_producto
    venta.id_empleado=id_empleado
    venta.id_cliente=id_cliente

    venta.save()
    return redirect('/')

def borrarVenta(request, id_venta):
    venta=Venta.objects.get(id_venta=id_venta)
    venta.delete()
    return redirect("/")
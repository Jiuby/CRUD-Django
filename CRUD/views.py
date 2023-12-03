from django.shortcuts import render, redirect
from  .models import usuario
# Create your views here.

def home(request):
    usuariosListados = usuario.objects.all()
    return render(request, "gestionUsuarios.html", {'usuarios':usuariosListados})

def registrarReal(request):
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    direccion = request.POST['txtDireccion']
    tarjeta_o_cedula = request.POST['txtTarjeta_o_cedula']
    Nombre_De_Ex = request.POST['txtNombreEx']
    fecha_nacimiento = request.POST['txtFechaCumple']

    Usuario=usuario.objects.create(
        nombre=nombre, apellido=apellido, direccion=direccion, tarjeta_o_cedula=tarjeta_o_cedula, Nombre_De_Ex=Nombre_De_Ex, fecha_nacimiento=fecha_nacimiento)
    return redirect('/')

def eliminarReal(request, nombre):
    Usuario=usuario.objects.get(nombre=nombre)
    Usuario.delete()
    return redirect('/')
    
def edicionReal(request, nombre):
    Usuario=usuario.objects.get(nombre=nombre)
    return render(request, "editarUsuario.html", {'usuario':Usuario})

def editarReal(request):
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    direccion = request.POST['txtDireccion']
    tarjeta_o_cedula = request.POST['txtTarjeta_o_cedula']
    Nombre_De_Ex = request.POST['txtNombreEx']
    fecha_nacimiento = request.POST['txtFechaCumple']

    Usuario=usuario.objects.get(nombre=nombre)
    Usuario.nombre=nombre
    Usuario.apellido=apellido
    Usuario.direccion=direccion
    Usuario.tarjeta_o_cedula=tarjeta_o_cedula
    Usuario.Nombre_De_Ex=Nombre_De_Ex
    Usuario.fecha_nacimiento=fecha_nacimiento
    Usuario.save()
    return redirect('/')
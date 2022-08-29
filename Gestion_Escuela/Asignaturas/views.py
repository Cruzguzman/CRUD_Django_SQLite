from django.shortcuts import render, redirect
from .models import Asignaturas
# Create your views here.
def home(request):
    lista_asignaturas=Asignaturas.objects.all()
    return render(request,"Gestion_Asignatura.html",{"L_Asignaturas":lista_asignaturas})


def registrarAsignatura(request):
    NDI=request.POST['txtDNI']
    Nombre = request.POST['txtNombre']
    Horas_t = request.POST['txtHoras_t']
    Horas_p = request.POST['txtHoras_p']
    Creditos = request.POST['txtCreditos']

    Guardar_asignatura=Asignaturas.objects.create(NDI=NDI,Nombre=Nombre,Horas_t=Horas_t,Horas_p=Horas_p,Creditos=Creditos)
    return redirect('/')

def eliminarAsignatura(request,NDI):
    Eliminar=Asignaturas.objects.get(NDI=NDI)
    Eliminar.delete()
    return redirect('/')

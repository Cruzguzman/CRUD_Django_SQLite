

from django.urls import path

from .import views

urlpatterns = [
    path('',views.home),
    path('registrarAsignatura/',views.registrarAsignatura),
    path('eliminarAsignatura/<NDI>',views.eliminarAsignatura),
   # path('editarAsignatura/<NDI>',views.editarAsignatura)

]
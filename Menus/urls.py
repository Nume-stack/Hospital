from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home ),
    path('contacto/', views.administrativo, name='contactoEmergencia' ),
    path('registrarContacto/', views.registrarContacto),
    path('contacto/eliminarContacto/<codigo>', views.eliminarConctacto),
    path('contacto/edicionContacto/<codigo>', views.edicionContacto),
    path('editarContacto/', views.editarConctacto),
    path('SeguroMedico/', views.segurosMedicos, name='seguros'),
    path('SeguroMedico/registrarSeguro/', views.registrarSeguro),
    path('SeguroMedico/eliminarSeguro/<codigo>', views.eliminarSeguros),
    path('SeguroMedico/edicionSeguro/<codigo>', views.edicionSeguros),
    path('editarSeguro/', views.editarSeguros),
    path('pacientes/', views.pacientes, name='pacientes'),
    path('pacientes/eliminarPaciente/<codigo>', views.eliminarPaciente),
    path('pacientes/registrarPaciente/', views.registrarPaciente),
    path('pacientes/edicionPaciente/<codigo>', views.edicionPaciente),
    path('editarPaciente/', views.EditarPaciente),
    path('usuarios/', views.RecursosHumanos, name='RecursosHumanos'),
    path('usuarios/registrarUsuario/', views.regitrarUsuarios),
    path('usuarios/eliminarUsuario/<codigo>', views.eliminarUsuario),
    path('usuarios/edicionUsuario/<codigo>', views.edicionUsuario),
    path('editarUsuario/', views.editarUsuario),
    path('citas/', views.pedirCitas, name='citas'),
    path('citas/registrarCita/', views.registrarCitas),
    path('citas/eliminarCita/<codigo>', views.eliminarCitas),
    path('citas/edicionCita/<codigo>', views.edicionCita),
    path('editarCita/', views.editarCita),
    path('historiaClinica/', views.HistoriaClinica, name='HistoriaC'),
    path('historiaClinica/registrarHistorial/', views.registrarHistoria),
    path('historiaClinica/eliminarHistoria/<codigo>', views.eliminarHistoria),
    path('visitas/', views.Visitas, name='visita'),
    path('visitas/registrarVisita/', views.RegistrarVisita),
    path('visitas/eliminarVisita/<codigo>', views.eliminarVisita),
    path('visitas/edicionVisita/<codigo>', views.edicionVisita),
    path('editarVisita/', views.editarVisita),
    path('entrar/', views.entrar),

    
]
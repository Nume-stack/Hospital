from django.shortcuts import render, redirect
from .models import *
from .models import paciente
import datetime

# Create your views here.
def entrar(request):
    nombre = request.POST['txtusername']
    paasword = request.POST['txtpassword']

    usuario = usuarios.objects.get(username = nombre)
    if usuario != None:
        if usuario.password == paasword:
            if usuario.rolUsuario == "Medico":
                return redirect('/historiaClinica/')
            else:
                if usuario.rolUsuario == "Administrativo":
                    return redirect('/contacto/')
                else:
                    if usuario.rolUsuario == "Enfermera":
                        return redirect('/visitas/')
                    else:
                        if usuario.rolUsuario == "Recursos Humanos":
                            return redirect('/usuarios/')
                        else:
                            return redirect('/')
    else:
        return redirect('/')
            
def editarVisita(request):
    id = request.POST['txtidVisitas']
    visita = visitas.objects.get(idVisitas = id)

    visita.fechaVisita = request.POST['txtfechaVisita']
    visita.datosVitales = request.POST['txtdatosVitales']
    visita.medicamentos = request.POST['txtMedicamento']
    visita.observaciones = request.POST['txtobservaciones']
    visita.recordatorios = request.POST['txtrecordatorios']
    visita.fechaRecordatorio = request.POST['txtfechaRecordatorio']
    visita.pruebas = request.POST['txtPruebas']
    visita.id_paciente = request.POST['txtPaciente']

    visita.save()
    return redirect('/visitas/')

def edicionVisita(request, codigo):
    visita = visitas.objects.get(idVisitas = codigo)
    pacientes = paciente.objects.all()
    return render(request, 'editarVisita.html', {"visita":visita, "pacientes" : pacientes})

def RegistrarVisita(request):
    visita = visitas.objects.create(
        fechaVisita = request.POST['txtfechaVisita'],
        datosVitales = request.POST['txtdatosVitales'],
        medicamentos = request.POST['txtMedicamento'],
        observaciones = request.POST['txtobservaciones'],
        recordatorios = request.POST['txtrecordatorios'],
        fechaRecordatorio = request.POST['txtfechaRecordatorio'],
        pruebas = request.POST['txtPruebas'],
        id_paciente = request.POST['txtPaciente']
    )
    visita.save()
    return redirect('/visitas/')

def eliminarVisita(reques, codigo):
    visita = visitas.objects.get(idVisitas = codigo)
    visita.delete()
    return redirect('/visitas/')

def Visitas(request):
    visita = visitas.objects.all()
    pacientes = paciente.objects.all()
    return render(request, 'visitas.html', {"visita":visita, "pacientes" : pacientes})

def edicionHistoral(request, codigo):
    historia = historiaClinica.objects.get(idHistoriaClinica = codigo)
    medicos = Medicos.objects.all()
    pacientes = paciente.objects.all()
    return render(request, 'HistoriasClinica.html', {"historia":historia, "medicos":medicos, "pacientes" : pacientes})

def eliminarHistoria(request, codigo):
    historia = historiaClinica.objects.get(idHistoriaClinica = codigo ) 
    historia.delete()
    return redirect('/historiaClinica/')

def registrarHistoria(request):
    historia = historiaClinica.objects.create(
        idPaciente = request.POST['txtPaciente'],
        idMedico  = request.POST['txtUsuario'],
        motivo = request.POST['txtMotivo'],
        diagnostico = request.POST['txtDiagnostico'],
        medicamento = request.POST['txtMedicamento'],
        ayudas_diagnosticas = request.POST['txtayudas_diagnosticas'],
        procedimiento = request.POST['txtprocedimiento']
    )
    historia.save()
    return redirect('/historiaClinica/')

def HistoriaClinica(request):
    historia = historiaClinica.objects.all()
    medicos = Medicos.objects.all()
    pacientes = paciente.objects.all()
    return render(request, 'HistoriasClinica.html', {"historia":historia, "medicos":medicos, "pacientes" : pacientes})
    
def editarCita(request):
    id = request.POST['txtIdCita']
    Cita = cita.objects.get(idCita = id)

    Cita.fechaCita = request.POST['txtFechaCita']
    Cita.id_Paciente = request.POST['txtPaciente']
    Cita.id_usuario= request.POST['txtUsuario']
    Cita.save()
    return redirect('/citas/')

def edicionCita (request, codigo):
    citasPacientes = cita.objects.get(idCita= codigo)
    medicos = Medicos.objects.all()
    pacientes = paciente.objects.all()
    return render(request, "editarCita.html", {"citas":citasPacientes, "medicos":medicos, "pacientes" : pacientes})

def eliminarCitas(request, codigo):
    DelCita = cita.objects.get(idCita = codigo)
    DelCita.delete()
    return redirect('/citas/')

def registrarCitas(request):
    PedirCita = cita.objects.create(
        fechaCita = request.POST['txtFechaCita'],
        id_Paciente = request.POST['txtPaciente'],
        id_usuario= request.POST['txtUsuario']
    )
    PedirCita.save()
    return redirect('/citas/')
    
def pedirCitas (request):
    citasPacientes = cita.objects.all()
    medicos = Medicos.objects.all()
    pacientes = paciente.objects.all()
    return render(request, "citas.html", {"citas":citasPacientes, "medicos":medicos, "pacientes" : pacientes})

def editarUsuario(request):
    codigo = request.POST['txtIdUsuario']
    rh = usuarios.objects.get(idUsuario = codigo)

    rh.nombreUsuario = str(request.POST['txtNombreContacto'])
    rh.identifiacionUsuario = str(request.POST['txtIdentificacion'])
    rh.correoUsuario = str(request.POST['txtCorreo'])
    rh.telefonoUsuario = str(request.POST['txtTelefono'])
    rh.fechaNacimientoUsuario = str(request.POST['txtNacimiento'])
    rh.direccionUsuario = str(request.POST['txtDireccion'])
    rh.rolUsuario = str(request.POST['txtRol'])
    rh.username = str(request.POST['txtUsername'])
    rh.password = str(request.POST['txtPassword'])
    rh.licencia = str(request.POST['txtLicencias'])
    

    rh.save()
    return redirect('/usuarios/')

def edicionUsuario(request, codigo):
    rh = usuarios.objects.get(idUsuario = codigo)
    return render(request, "editarUsuario.html", {"usuarios" : rh })

def eliminarUsuario(request, codigo):
    rh = usuarios.objects.get(idUsuario = codigo)
    rh.delete()
    if rh.rolUsuario == "Medico":
        medico = Medicos.objects.get( nombreMedico = rh.nombreUsuario )
        medico.delete()
    return redirect('/usuarios/')

def regitrarUsuarios(request):
    
    rh = usuarios.objects.create(
        nombreUsuario = request.POST['txtNombreContacto'],
        identifiacionUsuario = request.POST['txtIdentificacion'],
        correoUsuario = request.POST['txtCorreo'],
        telefonoUsuario = request.POST['txtTelefono'],
        fechaNacimientoUsuario = request.POST['txtNacimiento'],
        direccionUsuario = request.POST['txtDireccion'],
        rolUsuario = request.POST['txtRol'],
        username = request.POST['txtUsername'],
        password = request.POST['txtPassword'],
        licencia = request.POST['txtLicencias'],
        FechaAsistencia = datetime.datetime.now(),
        FechaCreacion = datetime.datetime.now()   
    )
    rol = request.POST['txtRol']
    if rol == "Medico":
        Medico = Medicos.objects.create(
            nombreMedico = request.POST['txtNombreContacto'],
            username = request.POST['txtUsername']
        )
    return redirect('/usuarios/')


def RecursosHumanos(request):
    rh = usuarios.objects.all()
    return render(request, "RecursosHumanos.html", {"usuarios":rh})

def EditarPaciente(request):
    codigo = request.POST['txtCodigo']
    pacientes = paciente.objects.get(idPaciente = codigo)

    pacientes.tipoIdentificacion  = request.POST['txtTipoIdentificacion']
    pacientes.nombrePaciente  = request.POST['txtNombrePaciente']
    pacientes.numeroIdentificacion  = request.POST['txtIdentificacion']
    pacientes.fecha_nacimiento  = request.POST['txtNacimiento']
    pacientes.generoPaciente  = request.POST['txtGenero']
    pacientes.direccionPaciente  = request.POST['txtDireccion']
    pacientes.correoPaciente  = request.POST['txtCorreo']
    pacientes.id_contactoEmergencia  = request.POST['txtIdContactoEmergencia']
    pacientes.id_seguroMedico  = request.POST['txtIdSeguro']

    pacientes.save()
    return redirect('/pacientes/')

def edicionPaciente(request,codigo):
    pacientes = paciente.objects.get(idPaciente = codigo)
    contactos = contacto_emergencia.objects.all()
    seguros = seguro_medico.objects.all()
    return render(request, "editarPaciente.html", {"pacientes" : pacientes, "contactos" : contactos,"seguros":seguros })

def editarSeguros(request):
    id = request.POST['txtCodigo']
    seguros = seguro_medico.objects.get(idSeguro = id)

    seguros.nombreCompañia = request.POST['txtSeguro']
    seguros.telefonoCompañia = request.POST['txtTelefono']
    seguros.save()
    return redirect('/SeguroMedico/')

def edicionSeguros(request, codigo):
    seguros = seguro_medico.objects.get(idSeguro = codigo)
    return render(request, "editarSeguros.html", {"seguros" : seguros })

def eliminarSeguros(request, codigo):
    seguros = seguro_medico.objects.get(idSeguro = codigo)
    seguros.delete()
    return redirect('/SeguroMedico/')

def registrarSeguro(request):
    nombreSeguro = request.POST['txtNombreSeguro']
    telefonoSeguro = request.POST['txtTelefonoSeguro']

    seguro = seguro_medico.objects.create( nombreCompañia = nombreSeguro, telefonoCompañia = telefonoSeguro)  

    return redirect('/SeguroMedico/')

def segurosMedicos(request):
    seguros = seguro_medico.objects.all()
    return render(request, "Seguros.html", {"seguros":seguros})

def administrativo(request):
    contactos = contacto_emergencia.objects.all()
    return render(request, "administrativos.html", {"contactos" : contactos })

def home(request):
    contactos = contacto_emergencia.objects.all()
    return render(request, "entrada.html", {"contactos" : contactos })

def registrarContacto(request):
    nombreContacto = request.POST['txtNombreContacto']
    TELEFONOContacto = request.POST['txtTelefonoContacto']
    relacionContacto = request.POST['txtRelacionContacto']

    contacto = contacto_emergencia.objects.create(NombreContactoEmergencia = nombreContacto, telefonoContactoEmergencia = TELEFONOContacto, relacionContactoEmergencia=relacionContacto )
    return redirect('/contacto/')

def eliminarConctacto(request, codigo):
    contacto = contacto_emergencia.objects.get(idContactoEmergencia=codigo)
    contacto.delete()
    return redirect('/contacto/')

def edicionContacto (request, codigo):
    contacto = contacto_emergencia.objects.get(idContactoEmergencia=codigo)
    return render(request, "editarContacto.html", {"contactos" : contacto })

def editarConctacto(request):
    id = request.POST['txtCodigo']
    nombreContacto = request.POST['txtNombreContacto']
    TELEFONOContacto = request.POST['txtTelefonoContacto']
    relacionContacto = request.POST['txtRelacionContacto']

    contacto = contacto_emergencia.objects.get(idContactoEmergencia=id)
    contacto.NombreContactoEmergencia = nombreContacto
    contacto.telefonoContactoEmergencia = TELEFONOContacto
    contacto.relacionContactoEmergencia = relacionContacto
    contacto.save()
    return redirect('/contacto/')

def pacientes(request):
    pacientes = paciente.objects.all()
    contactos = contacto_emergencia.objects.all()
    seguros = seguro_medico.objects.all()
    return render(request, "pacientes.html", {"pacientes" : pacientes, "contactos" : contactos,"seguros":seguros })

def eliminarPaciente(request,codigo):
    pacientes = paciente.objects.get(idPaciente=codigo)
    pacientes.delete()
    return redirect('/pacientes/')

def registrarPaciente (request):

    pacientes = paciente.objects.create(
        tipoIdentificacion  = request.POST['txtTipoIdentificacion'],
        nombrePaciente  = request.POST['txtNombrePaciente'],
        numeroIdentificacion  = request.POST['txtIdentificacion'],
        fecha_nacimiento  = request.POST['txtNacimiento'],
        generoPaciente  = request.POST['txtGenero'],
        direccionPaciente  = request.POST['txtDireccion'],
        correoPaciente  = request.POST['txtCorreo'],
        id_contactoEmergencia  = request.POST['txtIdContactoEmergencia'],
        id_seguroMedico  = request.POST['txtIdSeguro'],
    )
    return redirect('/pacientes/')
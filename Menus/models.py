from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
relacion_choice = (
    ('Madre', 'Madre'),
    ('Padre', 'Padre'),
    ('Hermano', 'Hermano'),
    ('Hijo', 'Hijo'),
    ('Otro', 'Otro')

)

tipo_identificacion = (
    ('CC', 'Cedula Ciudadana'),
    ('TI', 'Tarjeta Identidad'),
    ('CE', 'Cedula Extranjeria')
)

genero = (
    ('Masculino','Masculino'),
    ('Femenino','Femenino'),
    ('Otro','Otro')
)

roles =(
    ('Medico', 'Medico'),
    ('Enfermera', 'Enfermera'),
    ('Recursos Humanos', 'Recursos Humanos'),
    ('Administrativo', 'Administrativo')
)

class contacto_emergencia(models.Model):
    idContactoEmergencia = models.AutoField(primary_key=True)
    NombreContactoEmergencia = models.CharField(max_length=100, blank=False)
    telefonoContactoEmergencia = models.CharField(max_length=20, blank=False)
    relacionContactoEmergencia = models.CharField(max_length=50, blank=False, choices=relacion_choice)

    def __str__(self) :
        texto = "{0}"
        return texto.format(self.NombreContactoEmergencia)

class seguro_medico(models.Model):
    idSeguro = models.AutoField(primary_key=True)
    nombreCompañia = models.CharField(max_length=100, blank=False)
    telefonoCompañia = models.CharField(max_length=50, blank=False)
    def __str__(self) :
        texto = "{0}"
        return texto.format(self.nombreCompañia)



class paciente (models.Model):
    idPaciente = models.AutoField(primary_key=True)
    tipoIdentificacion = models.CharField(max_length=50, blank=False, choices=tipo_identificacion)
    nombrePaciente = models.CharField(max_length=100, default='ValorPredeterminado')
    numeroIdentificacion = models.CharField(max_length=50, blank=False)
    fecha_nacimiento = models.DateField(blank=False)
    generoPaciente = models.CharField(max_length=50, blank=False, choices=genero)
    direccionPaciente = models.CharField(max_length=100, blank=False)
    correoPaciente = models.EmailField(max_length=70, blank=False)
    id_contactoEmergencia = models.CharField(max_length=50, blank=False)
    id_seguroMedico = models.CharField(max_length=50, blank=False)
    def __str__(self) :
        texto = "{0}"
        return texto.format(self.nombrePaciente)

class visitas (models.Model):
    idVisitas = models.AutoField(primary_key=True)
    fechaVisita = models.DateTimeField(blank=False)
    datosVitales = models.CharField(max_length=100,blank=False)
    medicamentos = models.CharField(max_length=150, null=True)
    observaciones = models.CharField(max_length=200, blank=False)
    recordatorios = models.CharField(max_length=150, null=True)
    fechaRecordatorio = models.DateTimeField(null=True)
    pruebas = models.CharField(max_length=200, default="Prueba")
    id_paciente = models.CharField(max_length=50, blank=False)


class usuarios(models.Model):
    idUsuario = models.AutoField(primary_key=True)
    nombreUsuario = models.CharField(max_length=100, blank=False)
    identifiacionUsuario = models.CharField(max_length=20, blank=False)
    correoUsuario = models.EmailField(blank=False)
    telefonoUsuario = models.CharField(max_length=50, blank=False)
    fechaNacimientoUsuario = models.DateField(blank=False)
    direccionUsuario = models.CharField(max_length=100, blank=False)
    rolUsuario = models.CharField(max_length=50, blank=False, choices=roles)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    licencia = models.CharField(max_length=150)
    FechaAsistencia = models.DateTimeField(auto_now=True)
    FechaCreacion = models.DateTimeField(auto_now_add=True)


class cita (models.Model):
    idCita = models.AutoField(primary_key=True)
    fechaCita = models.DateTimeField(blank=False)
    id_Paciente = models.CharField(max_length=50, blank=False)
    id_usuario= models.CharField(max_length=50, blank=False)

class historiaClinica (models.Model):
    idHistoriaClinica = models.AutoField(primary_key=True)
    idPaciente = models.CharField(max_length=50, blank=False)
    idMedico  = models.CharField(max_length=50, blank=False)
    motivo = models.CharField(max_length=200)
    diagnostico = models.CharField(max_length=200)
    medicamento = models.CharField(max_length=200)
    ayudas_diagnosticas = models.CharField(max_length=200)
    procedimiento = models.CharField(max_length=200)

class Medicos(models.Model):
    nombreMedico = models.CharField(max_length=50, blank=False)
    username = models.CharField(max_length=50, blank=False)
    
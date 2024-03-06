from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(contacto_emergencia)
admin.site.register(seguro_medico)
admin.site.register(paciente)
admin.site.register(visitas)
admin.site.register(usuarios)
admin.site.register(cita)
admin.site.register(historiaClinica)
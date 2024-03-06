# Generated by Django 4.1.7 on 2023-11-17 03:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contacto_emergencia',
            fields=[
                ('idContactoEmergencia', models.AutoField(primary_key=True, serialize=False)),
                ('NombreContactoEmergencia', models.CharField(max_length=100)),
                ('telefonoContactoEmergencia', models.CharField(max_length=20)),
                ('relacionContactoEmergencia', models.CharField(choices=[('Madre', 'Madre'), ('Padre', 'Padre'), ('Hermano', 'Hermano'), ('Hijo', 'Hijo'), ('Otro', 'Otro')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='paciente',
            fields=[
                ('idPaciente', models.AutoField(primary_key=True, serialize=False)),
                ('tipoIdentificacion', models.CharField(choices=[('CC', 'Cedula Ciudadana'), ('TI', 'Tarjeta Identidad'), ('CE', 'Cedula Extranjeria')], max_length=50)),
                ('nombrePaciente', models.CharField(default='ValorPredeterminado', max_length=100)),
                ('numeroIdentificacion', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('generoPaciente', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], max_length=50)),
                ('direccionPaciente', models.CharField(max_length=100)),
                ('correoPaciente', models.EmailField(max_length=70)),
                ('id_contactoEmergencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menus.contacto_emergencia')),
            ],
        ),
        migrations.CreateModel(
            name='seguro_medico',
            fields=[
                ('idSeguro', models.AutoField(primary_key=True, serialize=False)),
                ('nombreCompañia', models.CharField(max_length=100)),
                ('telefonoCompañia', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombreUsuario', models.CharField(max_length=100)),
                ('identifiacionUsuario', models.CharField(max_length=20)),
                ('correoUsuario', models.EmailField(max_length=254)),
                ('telefonoUsuario', models.CharField(max_length=50)),
                ('fechaNacimientoUsuario', models.DateField()),
                ('direccionUsuario', models.CharField(max_length=100)),
                ('rolUsuario', models.CharField(choices=[('Medico', 'Medico'), ('Enfermera', 'Enfermera'), ('Recursos Humanos', 'Recursos Humanos'), ('Administrativo', 'Administrativo')], max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('licencia', models.CharField(max_length=150)),
                ('FechaAsistencia', models.DateTimeField(auto_now=True)),
                ('FechaCreacion', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='visitas',
            fields=[
                ('idVisitas', models.AutoField(primary_key=True, serialize=False)),
                ('fechaVisita', models.DateTimeField()),
                ('datosVitales', models.CharField(max_length=100)),
                ('medicamentos', models.CharField(max_length=150, null=True)),
                ('observaciones', models.CharField(max_length=200)),
                ('recordatorios', models.CharField(max_length=150, null=True)),
                ('fechaRecordatorio', models.DateTimeField(default=datetime.datetime(2023, 11, 16, 22, 7, 35, 644029))),
                ('pruebas', models.CharField(default='Prueba', max_length=200)),
                ('id_paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menus.paciente')),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='id_seguroMedico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menus.seguro_medico'),
        ),
        migrations.CreateModel(
            name='historiaClinica',
            fields=[
                ('idHistoriaClinica', models.AutoField(primary_key=True, serialize=False)),
                ('motivo', models.CharField(max_length=200)),
                ('diagnostico', models.CharField(max_length=200)),
                ('medicamento', models.CharField(max_length=200)),
                ('ayudas_diagnosticas', models.CharField(max_length=200)),
                ('procedimiento', models.CharField(max_length=200)),
                ('idMedico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menus.usuarios')),
                ('idPaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menus.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='cita',
            fields=[
                ('idCita', models.AutoField(primary_key=True, serialize=False)),
                ('fechaCita', models.DateTimeField()),
                ('id_Paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menus.paciente')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menus.usuarios')),
            ],
        ),
    ]
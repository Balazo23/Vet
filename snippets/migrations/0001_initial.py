# Generated by Django 5.1.7 on 2025-03-20 20:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Apellido_paterno', models.CharField(max_length=50)),
                ('Apellido_materno', models.CharField(max_length=50)),
                ('Fecha_nacimiento', models.DateField()),
                ('Rut', models.CharField(max_length=10)),
                ('Telefono', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254)),
                ('Sexo', models.CharField(max_length=50)),
                ('Estado_civil', models.CharField(max_length=50)),
                ('Direccion', models.CharField(max_length=100)),
                ('Ciudad', models.CharField(max_length=50)),
                ('Comuna', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_cita', models.DateTimeField()),
                ('Motivo', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Veterinarios',
            fields=[
                ('personas_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='snippets.personas')),
                ('Especialidad', models.CharField(max_length=50)),
            ],
            bases=('snippets.personas',),
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=200)),
                ('ConsultaId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snippets.consulta')),
            ],
        ),
        migrations.CreateModel(
            name='Mascotas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Fecha_nacimiento', models.DateField()),
                ('Raza', models.CharField(max_length=50)),
                ('Sexo', models.CharField(max_length=50)),
                ('Edad', models.IntegerField()),
                ('Estado_mascota', models.CharField(max_length=50)),
                ('Peso', models.FloatField()),
                ('Especie', models.CharField(max_length=200)),
                ('Persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snippets.personas')),
            ],
        ),
        migrations.AddField(
            model_name='consulta',
            name='MascotasId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snippets.mascotas'),
        ),
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('personas_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='snippets.personas')),
                ('Id_mascota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snippets.mascotas')),
            ],
            bases=('snippets.personas',),
        ),
        migrations.AddField(
            model_name='consulta',
            name='VeterinariosId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snippets.veterinarios'),
        ),
    ]

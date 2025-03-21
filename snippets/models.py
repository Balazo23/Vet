from django.db import models

# Create your models here.
"""
Luego de la creacion de clases realizar la siguiente lista
makemigrations
migrate
y registrarlas en el admin
"""


class Personas(models.Model):
    Nombre = models.CharField(max_length=50)
    Apellido_paterno = models.CharField(max_length=50)
    Apellido_materno = models.CharField(max_length=50)
    Fecha_nacimiento = models.DateField()
    Rut = models.CharField(max_length=10)
    Telefono = models.CharField(max_length=15)
    Email = models.EmailField()
    Sexo = models.CharField(max_length=50)
    Estado_civil = models.CharField(max_length=50)
    Direccion = models.CharField(max_length=100)
    Ciudad = models.CharField(max_length=50)
    Comuna = models.CharField(max_length=50)


class Mascotas(models.Model):
    Nombre = models.CharField(max_length=50)
    Fecha_nacimiento = models.DateField()
    Raza = models.CharField(max_length=50)
    Sexo = models.CharField(max_length=50)
    Edad = models.IntegerField()
    Persona = models.ForeignKey(Personas, on_delete=models.CASCADE)
    Estado_mascota = models.CharField(max_length=50)
    Peso = models.FloatField()
    Especie = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.Nombre} - {self.Especie} - {self.Raza} - {self.Sexo}"


class Clientes(Personas):
    Id_mascota = models.ForeignKey(Mascotas, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Nombre}"


class Veterinarios(Personas):
    Especialidad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Nombre}"


class Consultas(models.Model):
    Fecha_cita = models.DateTimeField()
    Motivo = models.CharField(max_length=200)
    VeterinariosId = models.ForeignKey(Veterinarios, on_delete=models.CASCADE)
    MascotasId = models.ForeignKey(Mascotas, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Fecha_cita}"


class Diagnosticos(models.Model):
    Descripcion = models.CharField(max_length=200)
    ConsultasId = models.ForeignKey(Consultas, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Fecha_hora}"

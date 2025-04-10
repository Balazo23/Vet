from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.models import User
from django.db.models import Sum
# Create your models here.
"""
Luego de la creacion de clases realizar la siguiente lista
makemigrations
migrate
y registrarlas en el admin
"""


class Mascotas(models.Model):
    nombre = models.TextField(null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    especie = models.TextField(null=True, blank=True)
    raza = models.TextField(null=True, blank=True)
    sexo = models.TextField(null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    peso = models.FloatField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.nombre:
            self.nombre = self.nombre.strip().title()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} ({self.raza})"


class Clientesdos(models.Model):
    nombre = models.TextField(null=True, blank=True)
    apellido_paterno = models.TextField(null=True, blank=True)
    apellido_materno = models.TextField(null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    rut = models.TextField(null=True, blank=True)
    telefono = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    sexo = models.TextField(null=True, blank=True)
    estado_civil = models.TextField(null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    ciudad = models.TextField(null=True, blank=True)
    comuna = models.TextField(null=True, blank=True)
    id_mascota = models.ForeignKey(
        Mascotas, on_delete=models.CASCADE, related_name="clientes", null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.email})"


class Veterinarios(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.TextField(null=True, blank=True)
    apellido_paterno = models.TextField(null=True, blank=True)
    apellido_materno = models.TextField(null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    rut = models.TextField(null=True, blank=True)
    telefono = models.TextField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    sexo = models.TextField(null=True, blank=True)
    estado_civil = models.TextField(null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    ciudad = models.TextField(null=True, blank=True)
    comuna = models.TextField(null=True, blank=True)
    especialidad = models.TextField(null=True, blank=True)  # hacer foreign
    num_colegiado = models.TextField(null=True, blank=True)
    mascotas = models.ManyToManyField(
        Mascotas, blank=True, through='Consultas')

    def __str__(self):
        return f"{self.nombre} ({self.especialidad})"


class Consultas(models.Model):
    ESTADOS = [
        ('PROGRAMADA', 'Programada'),
        ('EN_PROGRESO', 'En Progreso'),
        ('COMPLETADA', 'Completada'),
        ('CANCELADA', 'Cancelada'),
    ]

    fecha_cita = models.DateTimeField()
    motivo = models.TextField(null=True, blank=True)
    tratamiento = models.TextField(null=True, blank=True)
    diagnostico = models.TextField(blank=True, null=True)
    observaciones = models.TextField(null=True, blank=True)
    veterinario = models.ForeignKey(Veterinarios, on_delete=models.CASCADE)
    clientes = models.ForeignKey(Clientesdos, on_delete=models.CASCADE)
    estado = models.TextField(choices=ESTADOS, default='PROGRAMADA')
    mascotas = models.ForeignKey(
        Mascotas, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.motivo} ({self.mascotas})"


class Facturas(models.Model):
    ESTADOS_PAGO = [
        ('PENDIENTE', 'Pendiente'),
        ('PARCIAL', 'Parcial'),
        ('PAGADO', 'Pagado'),
    ]

    METODOS_PAGO = [
        ('EFECTIVO', 'Efectivo'),
        ('TARJETA', 'Tarjeta'),
        ('TRANSFERENCIA', 'Transferencia'),
    ]

    fecha = models.DateField(auto_now_add=True)
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)
    monto_pagado = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    estado_pago = models.TextField(
        choices=ESTADOS_PAGO, default='PENDIENTE', editable=False)
    metodo_pago = models.TextField(choices=METODOS_PAGO, blank=True, null=True)
    consultas = models.ForeignKey(
        Consultas, on_delete=models.CASCADE, related_name='factura')
    clientesdos = models.ForeignKey(
        Clientesdos, on_delete=models.CASCADE, related_name='facturas')

    total_deuda = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Calcular estado de pago automáticamente
        if self.monto_pagado == 0:
            self.estado_pago = 'PENDIENTE'
        elif self.monto_pagado >= self.monto_total:
            self.estado_pago = 'PAGADO'
            self.monto_pagado = self.monto_total
        else:
            self.estado_pago = 'PARCIAL'

        self.total_deuda = self.monto_total - self.monto_pagado
        super().save(*args, **kwargs)


class HistorialMedico(models.Model):
    mascota = models.ForeignKey(
        Mascotas, related_name='historial', on_delete=models.CASCADE, blank=True, null=True)
    enfermedades_cronicas = models.TextField(null=True, blank=True)
    alergias = models.TextField(null=True, blank=True)
    cirugias = models.TextField(null=True, blank=True)
    antecedentes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Historial Médico de {self.mascota.nombre}"


# owner = models.ForeignKey(
#     'auth.User', related_name='snippets', on_delete=models.CASCADE)
# highlighted = models.TextField()

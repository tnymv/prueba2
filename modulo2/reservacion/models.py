from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dpi_pasaporte = models.CharField(max_length=20)
    nit = models.CharField(max_length=20)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=200)
    nacionalidad = models.CharField(max_length=100)

class Habitacion(models.Model):
    TIPOS_HABITACION = [
        ('Simple', 'Simple'),
        ('Doble', 'Doble'),
        ('Triple', 'Triple'),
        ('Matrimonial', 'Matrimonial'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPOS_HABITACION)

class Reservacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    forma_pago = models.CharField(max_length=20)
    fecha_entrada = models.DateTimeField()
    fecha_salida = models.DateTimeField()
    num_huespedes_adultos = models.IntegerField()
    num_huespedes_ninos = models.IntegerField()
    edad_ninos = models.IntegerField()
    num_desayunos_buffete = models.IntegerField()
    dias_renta_auto = models.IntegerField(null=True, blank=True)
    codigo_tarifa = models.CharField(max_length=20, null=True, blank=True)
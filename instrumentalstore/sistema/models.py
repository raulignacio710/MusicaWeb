from django.db import models

# Create your models here.
class Mensaje(models.Model):
    codigoMensaje = models.AutoField(primary_key = True)
    nombreRemitente = models.CharField(max_length = 20)
    correo = models.EmailField(max_length = 30)
    mensaje = models.TextField()

class Cliente(models.Model):
    codigoCliente = models.AutoField(primary_key = True)
    run = models.CharField(max_length = 10)
    nombres = models.CharField(max_length = 20)
    apPaterno = models.CharField(max_length = 20)
    apMaterno = models.CharField(max_length = 20)

class Instrumento(models.Model):
    codigoInstrumento = models.AutoField(primary_key = True)
    marca = models.CharField(max_length = 20)
    modelo = models.CharField(max_length = 20)
    serie = models.CharField(max_length = 15)
    tipo = models.CharField(max_length = 20)
    descripcion = models.TextField()
    precio = models.IntegerField()
    stock = models.IntegerField()

class Venta(models.Model):
    codigoVenta = models.AutoField(primary_key = True)
    cliente = models.ForeignKey(Cliente, on_delete = models.DO_NOTHING)
    instrumento = models.ForeignKey(Instrumento, on_delete = models.DO_NOTHING)
    fecha = models.DateField()

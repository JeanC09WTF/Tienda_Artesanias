from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="Descripción del producto")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=100, default="General")

    def __str__(self):
        return self.name

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(default="Descripción del producto")
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/')
    categoria = models.CharField(max_length=100, default="General")

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    fecha = models.DateField()
    hora = models.TimeField()
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Reserva de {self.nombre} para {self.fecha} a las {self.hora}"

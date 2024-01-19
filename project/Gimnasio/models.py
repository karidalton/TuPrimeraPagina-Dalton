from django.db import models


class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    domicilio = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre}"

class Plan(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.nombre}"
    
    class Meta:
        verbose_name = "plan"
        verbose_name_plural = "Planes"

class Suscriptor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    alta = models.DateField()
    
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    class Meta:
        verbose_name = "suscriptor"
        verbose_name_plural = "sucriptores"


class SuscriptoPorSede(models.Model):
    cliente = models.ForeignKey(Suscriptor, on_delete=models.CASCADE)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.sede}: {self.cliente}"
    
    class Meta:
        verbose_name = "suscriptor por sede"
        verbose_name_plural = "sucriptores por sede"


class SuscriptoPorPLan(models.Model):
    cliente = models.ForeignKey(Suscriptor, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.plan}: {self.cliente}"
    class Meta:
        verbose_name = "suscriptor por plan"
        verbose_name_plural = "suscriptores por plan"

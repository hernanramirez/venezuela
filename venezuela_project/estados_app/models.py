from django.db import models


class Estado (models.Model):
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre


class Municipio (models.Model):
    estado = models.ForeignKey(Estado)
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre


class Parroquia (models.Model):
    municipio = models.ForeignKey(Municipio)
    nombre = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nombre

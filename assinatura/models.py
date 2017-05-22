# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models




def scramble_assinatura_filename(instance, filename):
    extension = filename.split(".")[1]
    return "{}.{}".format(uuid.uuid4(), extension)

# Create your models here.

class Assinatura(models.Model):
    image = models.ImageField('Uploaded Image', upload_to=scramble_assinatura_filename)

class Documento(models.Model):
    data = models.DateField(auto_now=True)
    numero = models.PositiveIntegerField()
    entregue = models.BooleanField(default=False)
    recibo = models.FileField(upload_to=scramble_assinatura_filename, blank=True)

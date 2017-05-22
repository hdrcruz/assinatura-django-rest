# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from assinatura.models import Assinatura, Documento

# Register your models here.

admin.site.register(Assinatura)
admin.site.register(Documento)

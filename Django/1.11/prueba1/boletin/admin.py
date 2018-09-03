# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Registrado #Se importa el modelo

admin.site.register(Registrado) #anade el modelo creado a nuestra ventana de admin
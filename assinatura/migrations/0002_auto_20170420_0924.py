# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 09:24
from __future__ import unicode_literals

import assinatura.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assinatura', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assinatura',
            name='image',
            field=models.ImageField(upload_to=assinatura.models.scramble_assinatura_filename, verbose_name='Uploaded Image'),
        ),
    ]
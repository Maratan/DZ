# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-29 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DZ', '0003_auto_20161128_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='tovar',
            name='name',
            field=models.CharField(default=1, max_length=70, verbose_name='Название'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tovar',
            name='image',
            field=models.ImageField(upload_to='image', verbose_name='Картинка'),
        ),
    ]

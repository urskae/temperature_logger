# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blaziot', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Temperature',
            new_name='Temp',
        ),
        migrations.RenameField(
            model_name='temp',
            old_name='temperature_value',
            new_name='temp_value',
        ),
        migrations.RenameField(
            model_name='temp',
            old_name='measured_date',
            new_name='time_measured',
        ),
    ]

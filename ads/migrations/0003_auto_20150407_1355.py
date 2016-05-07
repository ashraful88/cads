# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_auto_20150407_1344'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-created'], 'verbose_name': 'Ad Entry', 'verbose_name_plural': 'Ad Entries'},
        ),
    ]

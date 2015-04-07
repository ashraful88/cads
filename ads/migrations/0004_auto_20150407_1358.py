# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_auto_20150407_1355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['parent'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]

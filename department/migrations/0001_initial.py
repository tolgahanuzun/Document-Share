# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('departmenStasion', models.CharField(max_length=50, verbose_name=b'Departman Name')),
                ('departmenMembers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name=b'Departmen \xc4\xb0n Members', blank=True)),
            ],
        ),
    ]

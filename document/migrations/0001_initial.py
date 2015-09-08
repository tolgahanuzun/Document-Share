# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('department', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Document Name')),
                ('description', models.TextField(max_length=1000, verbose_name='Document description')),
                ('createtime', models.DateTimeField(verbose_name=b'Document Add Time')),
                ('doc_file', models.FileField(upload_to=b'documentfiles/', verbose_name=b'Document Update')),
                ('send_Department', models.ManyToManyField(to='department.Department', verbose_name=b'Send To Department')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.
class Document(models.Model):
    name = models.CharField(max_length=50,verbose_name="Document Name")
    description = models.TextField(max_length=1000, verbose_name=u"Document description")
    createtime = models.DateTimeField(auto_now_add=True,verbose_name="Document Add Time")
    doc_file = models.FileField(upload_to="documentfiles/" ,verbose_name="Document Update")
    user = models.ForeignKey(User)
    send_Department = models.ManyToManyField("department.Department", verbose_name="Send To Department")
    
    def __unicode__(self):
        return "%s" % (self.name)

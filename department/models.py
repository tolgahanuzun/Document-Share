# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    departmenStasion = models.CharField(max_length=50,verbose_name="Departman Name")
    departmenMembers = models.ManyToManyField(User,blank=True ,verbose_name="Departmen İn Members")

    def __unicode__(self):
        return "%s" % (self.departmenStasion)



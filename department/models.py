# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    department_Name = models.CharField(max_length=50,verbose_name="Departman Name")
    department_Members = models.ManyToManyField(User,blank=True ,verbose_name="Departmen İn Members")

    def __unicode__(self):
        return "%s" % (self.department_Name)



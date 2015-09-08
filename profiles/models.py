# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.OneToOneField(User)
	#Kullanıcı modelini Djangonun kendi yapısıyla kullandım. İhtiyacım olan herşey orda var. 
	#Departman app'inde oluşturduğum bölümleri burada seçenek halinde çektim.

	my_Document = models.ManyToManyField('document.Document',blank=True, verbose_name="My Document")

	def __unicode__(self):
		return "%s" % (self.user)



# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class employees(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    emp_id=models.IntegerField()
    def __str__(self):
        return self.firstname

class videos(models.Model):
    title=models.CharField(max_length=15)
    description=models.TextField()
    album=models.CharField(max_length=20)
    extra=models.CharField(max_length=20)
    offer=models.BooleanField(default=False)
    cont=models.ImageField(upload_to='pics')
    videofile = models.FileField(upload_to='videos', null=True, verbose_name="video_file")


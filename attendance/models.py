from django.db import models
from django.contrib.auth.models import User
from main.models import *


import datetime
from time import time

from django.db import models




types = [('student','student'),('teacher','teacher')]
class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    status = models.CharField(choices=types,max_length=20,null=True,blank=False,default='employee')
    present = models.BooleanField(default=False)
    image = models.ImageField()
    updated = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.first_name +' '+self.last_name


class LastFace(models.Model):
    last_face = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.last_face


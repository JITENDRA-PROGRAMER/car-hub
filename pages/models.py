from datetime import datetime
from distutils.command.upload import upload
from django.db import models

# Create your models here.

# Team models
class Team(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='photos/%y/%m/%d/')
    facebook_link = models.URLField(max_length=100)
    twiter_link = models.URLField(max_length=100)
    linkdin_link = models.URLField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

    # return firstname as a database
    def __str__(self):           
        return self.firstname
    
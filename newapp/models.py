from django.db import models

# Create your models here.

class submit(models.Model):
    email = models.EmailField()
    password = models.IntegerField()
    repassword = models.IntegerField()
    person_select = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    fgender = models.CharField(max_length=20)
    religion = models.CharField(max_length=30)
    language = models.CharField(max_length=20)

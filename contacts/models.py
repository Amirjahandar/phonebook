import email
from django.db import models

class Contact(models.Model):
    firsname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=70)
    tell = models.CharField(max_length=11)
    email = models.EmailField()

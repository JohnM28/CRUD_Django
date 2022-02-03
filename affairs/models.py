from django.db import models

# Create your models here.
class myuser(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.CharField(max_length=20)


from django.db import models

# Create your models here.
class myuser(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.CharField(max_length=20)


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    track = models.CharField(max_length=20)

class Intake(models.Model):
    id =models.AutoField(primary_key=True)
    name =models.CharField(max_length=20)
    start_date =models.DateField()
    end_date =models.DateField()


class Track(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
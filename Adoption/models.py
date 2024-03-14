from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class user(models.Model):
    userid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=25)


class Animal(models.Model):
    animalid = models.AutoField(primary_key=True)
    img = models.ImageField(upload_to='static/')
    species = models.CharField(max_length=20)
    breed = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    description = models.TextField()
    location = models.CharField(max_length=100, default='unknown')
    contact = models.BigIntegerField(null=True)
    availabilitystatus = models.BooleanField()
    uploadedby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Location(models.Model):
    location = models.CharField(max_length=100)
    postal_code = models.IntegerField()


class shelter(models.Model):
    shelterid = models.IntegerField()
    sheltername = models.CharField(max_length=100)
    contactinfo = models.IntegerField()


class AdoptionReq(models.Model):
    requestid = models.IntegerField()
    animalid = models.ForeignKey(Animal, on_delete=models.SET_NULL, null = True)
    requestinguserid = models.IntegerField()
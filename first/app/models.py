from django.db import models

# Create your models here.
class new(models.Model):
    name=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    chemistry=models.CharField(max_length=30)
    physics=models.CharField(max_length=30)
    maths=models.CharField(max_length=30)
    english=models.CharField(max_length=30)   
    email=models.EmailField(max_length=30)  
class new1(models.Model):
    username=models.CharField(max_length=30)
    password1=models.CharField(max_length=30)

class new2(models.Model):
    cname=models.CharField(max_length=30)
    cemail=models.CharField(max_length=30)
    cnumber=models.CharField(max_length=30)
    csub=models.CharField(max_length=30)
    cmessage=models.CharField(max_length=30)



     
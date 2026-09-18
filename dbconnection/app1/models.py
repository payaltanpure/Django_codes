from django.db import models

# Create your models here.

# class createdv\ to create table of same name 
class student(models.Model):

    # fields columns of database table created 

    name= models.CharField(max_length=20)
    lname= models.CharField(max_length=20)

    # def __str__(self):
    #     return self.name
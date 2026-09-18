from django.db import models

# Create your models here.

class student(models.Model):

    # fields columns of database table created 

    name= models.CharField(max_length=20)
    marks= models.IntegerField()

    def __str__(self):
        return self.name
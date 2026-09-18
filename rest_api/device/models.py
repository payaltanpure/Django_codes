from django.db import models

# Create your models here.
class device(models.Model):
    name = models.CharField()
    price = models.IntegerField()
    brand = models.CharField()

    def __str__(self):
        return self.name
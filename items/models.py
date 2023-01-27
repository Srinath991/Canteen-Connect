from django.db import models
from random import randint
class item(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(default='CEC tasty items',max_length=40)
    image=models.ImageField(upload_to='items')
    prize=models.PositiveSmallIntegerField()
    categoryID=models.PositiveSmallIntegerField()
    rating=models.FloatField()
    available=models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.name
# Create your models here.

from django.db import models
from items.models import item
from orders.models import order
# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    password=models.CharField(max_length=20,default='')
    phone=models.PositiveIntegerField()
    cart=models.ManyToManyField(item)
    order=models.ManyToManyField(order)
    def __str__(self) -> str:
        return self.name
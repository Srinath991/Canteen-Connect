from django.db import models
# Create your models here.
class order(models.Model):
    customer_id=models.CharField(max_length=10)
    product_id=models.PositiveSmallIntegerField()
    order_id=models.CharField(max_length=20)
    date_created=models.DateTimeField()
    date_delivary=models.DateTimeField()
    total_prize=models.PositiveSmallIntegerField()
    quantity=models.PositiveSmallIntegerField()
    def __str__(self) -> str:
        return self.order_id

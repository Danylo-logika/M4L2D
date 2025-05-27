from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank = True)
    price = models.DecimalField()

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    text = models.TextField(null=True, blank = True)
    rating = models.IntegerField(default=0)
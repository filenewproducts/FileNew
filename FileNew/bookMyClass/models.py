from django.db import models


# Create your models here.
class ProductType(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField('date publisbed')

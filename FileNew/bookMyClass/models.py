from django.db import models
from django.utils import timezone
# Create your models here.


class ProductType(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(
        default=timezone.now, auto_now=False, auto_now_add=False)

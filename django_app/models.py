from django.db import models

# Create your models here.

class ScrapedProducts(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    condition = models.CharField(max_length=100, null=True, blank=True)
    selling_status = models.CharField(max_length=200, null=True, blank=True)

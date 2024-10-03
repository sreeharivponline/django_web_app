# store/models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)  # Image field
    video = models.FileField(upload_to='videos/', null=True, blank=True)  # Optional video field
    
    def __str__(self):
        return self.name
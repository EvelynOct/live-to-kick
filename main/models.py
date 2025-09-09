# Create your models here.
import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('transfer', 'Transfer'),
        ('update', 'Update'),
        ('exclusive', 'Exclusive'),
        ('match', 'Match'),
        ('rumor', 'Rumor'),
        ('analysis', 'Analysis'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255) # product name
    price = models.IntegerField() # product price
    description = models.TextField() # item description
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update') # product category
    thumbnail = models.URLField(blank=True, null=True) # product image
    is_featured = models.BooleanField(default=False) # featured product
    views = models.IntegerField(default=0) # number of views

    def __str__(self):
        return self.title

    @property
    def popular_item(self):
        return self.views > 50

    def increment_views(self):
        self.views += 1
        self.save()
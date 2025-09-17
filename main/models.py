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
    name = models.CharField(max_length=255) # product name (this was title)
    price = models.IntegerField(default=0) # product price
    description = models.TextField() # item description (this was content)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update') # product category
    thumbnail = models.URLField(blank=True, null=True) # product image
    is_featured = models.BooleanField(default=False) # featured product
    product_views = models.IntegerField(default=0) # number of views (this was news_views)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def popular_item(self):
        return self.product_views > 50

    def increment_views(self):
        self.product_views += 1
        self.save()
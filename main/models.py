import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [("sepatu lari", "Running Shoes"),
                        ("sepatu bola", "Football Shoes"),
                        ("jersey bola", "Football Jersey")]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default="sepatu bola")
    is_featured = models.BooleanField(default=False)
    brand = models.CharField(max_length=255)
    stock = models.IntegerField()

    def __str__(self):
        return self.name
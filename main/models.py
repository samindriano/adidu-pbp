import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [("sepatu lari", "Sepatu Lari"),
                        ("sepatu bola", "Sepatu Bola"),
                        ("kaus kaki", "Kaus Kaki"),
                        ("jersey bola", "Jersey Bola")]

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
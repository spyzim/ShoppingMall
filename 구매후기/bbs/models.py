from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.

class Review(models.Model):
    content = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d", blank=True, null=True)
    photo_thumbnail = ImageSpecField(source='photo', processors=[ResizeToFill(180,150)], format='JPEG')
    OPTIONS = (
        ("★★★★★","★★★★★"),
        ("★★★★☆","★★★★☆"),
        ("★★★☆☆","★★★☆☆"), 
        ("★★☆☆☆","★★☆☆☆"),
        ("★☆☆☆☆","★☆☆☆☆"), 
    )
    rating = models.CharField(default = 0, max_length = 10, choices=OPTIONS)
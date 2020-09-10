from django.db import models

# Create your models here.

class Review(models.Model):
    content = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d", blank=True, null=True)   # upload_to='timeline_photo/%Y/%m/%d'
    rating = models.PositiveIntegerField(default = 0)

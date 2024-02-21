# reviews/models.py
from django.db import models
from django.contrib.auth.models import User

class TouristReview(models.Model):
    user = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField()
    image = models.ImageField(upload_to='static/review_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review - {self.created_at}'

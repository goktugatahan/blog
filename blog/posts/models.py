from datetime import date
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.headline

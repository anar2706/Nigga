from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

class Tweet(models.Model):
    user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    content = models.CharField(max_length=256,unique=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def get_absolute_url(self):
        return reverse('tweets:detail',kwargs={'pk':self.pk})
    
    


    def __str__(self):
        return self.content


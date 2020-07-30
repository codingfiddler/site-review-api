from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Website(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    domain = models.CharField(max_length = 100)

class Page(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    
    pageURL = models.CharField(max_length=100)
    visitorCount = models.IntegerField()
    timeOnPage = models.IntegerField()
    creationDate = models.CharField(max_length=100)
    reviewerScore = models.IntegerField()

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    text = models.CharField(max_length = 100)




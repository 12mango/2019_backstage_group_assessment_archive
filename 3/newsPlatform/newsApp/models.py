from django.db import models

class news(models.Model):
    type=models.IntegerField()
    date=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=10000)

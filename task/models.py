from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=400)
    date = models.DateField(auto_now=False, auto_now_add=False)

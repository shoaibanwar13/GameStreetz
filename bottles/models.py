from django.db import models

class Player(models.Model):
    email=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.email
class Score(models.Model):
    email=models.CharField(max_length=100,primary_key=True)
    score=models.IntegerField(default=0)
    def __str__(self):
        return self.email

# Create your models here.

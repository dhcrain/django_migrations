from django.db import models

# Create your models here.

class TakeThree(models.Model):
    full_name = models.CharField(max_length=30)
    position = models.CharField(max_length=6)
    number = models.IntegerField()
    avg = models.FloatField()
    hr = models.IntegerField()
    rbi = models.IntegerField()
    runs = models.IntegerField()

    def __str__(self):
        return self.full_name

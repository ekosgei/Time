from django.db import models

class TimeActivity(models.Model):
    dayone = models.DateTimeField()
    numberofsessions = models.IntegerField()
    name = models.CharField(primary_key=True, max_length=100)
    
    


from django.db import models

class TimeActivity(models.Model):
    dayone = models.DateTimeField()
    numberofsessions = models.IntegerField()
    name = models.CharField(primary_key=True, max_length=100)
    
class TimeSession(models.Model):
    session_date = models.DateTimeField(primary_key=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    activity = models.ForeignKey(
        TimeActivity,
        on_delete=models.CASCADE
    )

class Name(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)


from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Define the team model, so user can view team tasks if he knows team name and password.
class Team(models.Model):
    # Stores the name of the team
    name = models.CharField(max_length=100)
    # Stores the password that is required to enter the team task system. Null and blank should be set to True.
    password = models.CharField(max_length=255, null=True, blank=True)
    # Checks if user is in a team
    in_team = models.BooleanField(default=False)

# Define the task model
class Tasks(models.Model):
    # Stores the titles of the tasks
    name = models.CharField(max_length=200)
    # Stores the description of the task
    description = models.TextField()
    # Stores the exact time when the task was created
    time = models.DateTimeField(default=datetime.now)
    # Checks if the task was completed 
    completed = models.BooleanField(default=False)




    

    
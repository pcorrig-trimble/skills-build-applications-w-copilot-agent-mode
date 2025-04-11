from djongo import models

class User(models.Model):
    id = models.ObjectIdField(primary_key=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    members = models.ArrayField(model_container=User)

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True)
    user_id = models.ObjectIdField()
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True)
    user_id = models.ObjectIdField()
    score = models.IntegerField()

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
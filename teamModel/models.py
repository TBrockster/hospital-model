from django.db import models

# Create your models here.

class TeamMember(models.Model):
    profilePicture = models.URLField()
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    onLeave = models.BooleanField()
    specialities = models.CharField(max_length=255)
    biography = models.TextField()

    def __str__(self):
        return self.firstName

class Team(models.Model):
    teamMembers = models.ManyToManyField(TeamMember)

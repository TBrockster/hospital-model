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
        full_name = self.firstName + ' ' + self.lastName
        return full_name

class Team(models.Model):
    teamName = models.CharField(max_length=255, unique=True)
    teamMembers = models.ManyToManyField(TeamMember)

    def __str__(self):
        return self.teamName
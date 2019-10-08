from django.db import models

# Create your models here.

class TeamMember(models.Model):
    TYPES = (
        ('Surgeon'),
        ('Nurse'),
        ('Admin Assistant'),
    )
    profilePicture = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=TYPES)
    onLeave = models.BooleanField
    specialities = models.CharField(max_length=255)
    biography = models.TextField

class Team(models.Model):
    teamMembers = models.ManyToManyField(TeamMember)

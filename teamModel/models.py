from django.db import models

# Create your models here.

class TeamMember():
  def __init__(self, firstName, lastName, specialities, biography):
    self.firstName = firstName
    self.lastName = lastName
    self.specialities = specialities
    self.biography = biography
    self.onLeave = False

  def toggleOnLeave(self):
    self.onLeave = (True, False)[self.onLeave]
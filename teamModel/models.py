from django.db import models

# Create your models here.

class TeamMember():
  def __init__(self, firstName, lastName, specialities):
    self.firstName = firstName
    self.lastName = lastName
    self.specialities = specialities
    self.onLeave = False

  def toggleOnLeave(self):
    self.onLeave = (True, False)[self.onLeave]
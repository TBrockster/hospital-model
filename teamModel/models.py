from django.db import models

# Create your models here.

class TeamMember():
  def __init__(self, firstName, lastName):
    self.firstName = firstName
    self.lastName = lastName
    self.onLeave = False

  def toggleOnLeave(self):
    self.onLeave = True
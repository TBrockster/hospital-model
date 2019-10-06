from django.db import models

# Create your models here.

class TeamMember():
  def __init__(self, firstName, lastName):
    self.firstName = firstName
    self.lastName = lastName
    self.onLeave = False

  def toggleOnLeave(self):
    if self.onLeave == True:
      self.onLeave = False
    else:
      self.onLeave = True

from django.db import models

# Create your models here.

class TeamMember():
    def __init__(self, first_name, last_name, type, specialities, biography):
        self.first_name = first_name
        self.last_name = last_name
        self.type = type
        self.specialities = specialities
        self.biography = biography
        self.on_leave = False

    def toggle_on_leave(self):
        self.on_leave = (True, False)[self.on_leave]

class Team():
    def __init__(self):
        self.roster = []

    def add_member(self, team_member):
        self.roster.append(team_member)
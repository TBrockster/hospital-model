from django.db import models

# Create your models here.

class TeamMember():
    def __init__(self, first_name, last_name, specialities, biography):
        self.first_name = first_name
        self.last_name = last_name
        self.specialities = specialities
        self.biography = biography
        self.on_leave = False
        self.teams = []

    def toggle_on_leave(self):
        self.on_leave = (True, False)[self.on_leave]

class Surgeon(TeamMember):
    def __init__(self, first_name, last_name, specialities, biography):
      TeamMember.__init__(self, first_name, last_name, specialities, biography)
      self.type = 'Surgeon'

class Nurse(TeamMember):
    def __init__(self, first_name, last_name, specialities, biography):
          TeamMember.__init__(self, first_name, last_name, specialities, biography)
          self.type = 'Nurse'

class AdminAssistant(TeamMember):
    def __init__(self, first_name, last_name, specialities, biography):
          TeamMember.__init__(self, first_name, last_name, specialities, biography)
          self.type = 'Admin Assistant'

class Team():
    def __init__(self):
        self.roster = []

    def add_member(self, team_member):
        team_member_check = self.check_team_member_teams_count(team_member)
        if team_member_check == False:
            raise Exception('Failed to add Team Member, already in maximum number of Teams')
        else:
            team_member.teams.append(self)
            self.roster.append(team_member)

    def check_team_member_teams_count(self, team_member):
        if team_member.type == 'Nurse' or team_member.type == 'Admin Assistant':
            result = (False, True)[len(team_member.teams) <= 2]
            return result
        elif team_member.type == 'Surgeon':
            result = (False, True)[len(team_member.teams) <= 0]
            return result
        else:
            return False

    def validity_check(self):
        type_count = self.roster_type_count()
        if type_count['Surgeon'] == 1 and type_count['Nurse'] >= 1 and type_count['Admin Assistant'] <= 1:
            return True
        else:
            return False

    def roster_type_count(self):
        team_count = {
          'Surgeon' : 0,
          'Nurse' : 0,
          'Admin Assistant' : 0
        }
        for team_member in self.roster:
            team_count[team_member.type] += 1
        return team_count
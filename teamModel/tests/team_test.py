from teamModel.models import Team
from teamModel.models import TeamMember

surgeon = TeamMember(first_name = 'John', 
                     last_name = 'Doe',
                     specialities = ['Renal', 'Paediatrics'],
                     biography = 'Lorem Ipsum')

nurse = TeamMember(first_name = 'Jane', 
                   last_name = 'Doe',
                   specialities = ['Renal', 'Paediatrics'],
                   biography = 'Lorem Ipsum')

admin_assistant = TeamMember(first_name = 'Jack', 
                             last_name = 'Doe',
                             specialities = ['Renal', 'Paediatrics'],
                             biography = 'Lorem Ipsum')

def test_TeamHasRoster():
  team = Team()
  assert team.roster == []

def test_TeamCanAddMembers():
  team = Team()
  team.add_member(surgeon)
  assert team.roster == [surgeon]

def test_TeamHasValidityCheck():
  team = Team()
  team.add_member(surgeon)
  assert team.validity_check() == False

def test_OneSurgeonOneNurse():
  team = Team()
  team.add_member(surgeon)
  team.add_member(nurse)
  assert team.validity_check() == True

def test_MaxOneSurgeon():
  team = Team()
  team.add_member(nurse)
  team.add_member(surgeon)
  team.add_member(surgeon)
  assert team.validity_check() == False

def test_OneAdminAssistant():
  team = Team()
  team.add_member(surgeon)
  team.add_member(nurse)
  team.add_member(admin_assistant)
  assert team.validity_check() == True

def test_MaxOneAdminAssistant():
  team = Team()
  team.add_member(surgeon)
  team.add_member(nurse)
  team.add_member(admin_assistant)
  team.add_member(admin_assistant)
  assert team.validity_check() == False

def test_UnlimitedNurses():
  team = Team()
  team.add_member(surgeon)
  team.add_member(nurse)
  team.add_member(nurse)
  assert team.validity_check() == True
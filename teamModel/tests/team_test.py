from teamModel.models import Team
from teamModel.models import TeamMember

john = TeamMember(first_name = 'John', 
                  last_name = 'Doe',
                  type = 'Surgeon',
                  specialities = ['Renal', 'Paediatrics'],
                  biography = 'Lorem Ipsum')

jane = TeamMember(first_name = 'Jane', 
                  last_name = 'Doe',
                  type = 'Nurse',
                  specialities = ['Renal', 'Paediatrics'],
                  biography = 'Lorem Ipsum')

jack = TeamMember(first_name = 'Jack', 
                  last_name = 'Doe',
                  type = 'Admin Assistant',
                  specialities = ['Renal', 'Paediatrics'],
                  biography = 'Lorem Ipsum')

def test_TeamHasRoster():
  team = Team()
  assert team.roster == []

def test_TeamCanAddMembers():
  team = Team()
  team.add_member(john)
  assert team.roster == [john]

def test_TeamHasValidityCheck():
  team = Team()
  team.add_member(john)
  assert team.validity_check() == False

def test_OneSurgeonOneNurse():
  team = Team()
  team.add_member(john)
  team.add_member(jane)
  assert team.validity_check() == True

def test_MaxOneSurgeon():
  team = Team()
  team.add_member(john)
  team.add_member(john)
  assert team.validity_check() == False

def test_OneAdminAssistant():
  team = Team()
  team.add_member(john)
  team.add_member(jane)
  team.add_member(jack)
  assert team.validity_check() == True
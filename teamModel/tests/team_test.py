from teamModel.models import Team
from teamModel.models import TeamMember

john = TeamMember(first_name = 'John', 
                  last_name = 'Doe',
                  type = 'Surgeon',
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
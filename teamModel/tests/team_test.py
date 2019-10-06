import pytest
from teamModel.models import Team, Surgeon, Nurse, AdminAssistant


surgeon = Surgeon(first_name = 'John', 
                  last_name = 'Doe',
                  specialities = ['Renal', 'Paediatrics'],
                  biography = 'Lorem Ipsum')

nurse = Nurse(first_name = 'Jane', 
              last_name = 'Doe',
              specialities = ['Renal', 'Paediatrics'],
              biography = 'Lorem Ipsum')

admin_assistant = AdminAssistant(first_name = 'Jack', 
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
  nurse = Nurse(first_name = 'Jane', 
                last_name = 'Doe',
                specialities = ['Renal', 'Paediatrics'],
                biography = 'Lorem Ipsum')
  team.add_member(nurse)
  team.add_member(admin_assistant)
  team.add_member(admin_assistant)
  assert team.validity_check() == False

def test_UnlimitedNurses():
  team = Team()
  team.add_member(surgeon)
  nurse = Nurse(first_name = 'Jane', 
                last_name = 'Doe',
                specialities = ['Renal', 'Paediatrics'],
                biography = 'Lorem Ipsum')
  team.add_member(nurse)
  team.add_member(nurse)
  assert team.validity_check() == True

def test_AddMemberAddsTeamToMembersTeamList():
  team = Team()
  nurse = Nurse(first_name = 'Jane', 
                last_name = 'Doe',
                specialities = ['Renal', 'Paediatrics'],
                biography = 'Lorem Ipsum')
  team.add_member(nurse)
  assert len(nurse.teams) == 1

def test_NurseInUpToThreeTeams():
  team_one = Team()
  team_two = Team()
  team_three = Team()
  team_four = Team()
  nurse = Nurse(first_name = 'Jane', 
                last_name = 'Doe',
                specialities = ['Renal', 'Paediatrics'],
                biography = 'Lorem Ipsum')
  team_one.add_member(nurse)
  team_two.add_member(nurse)
  team_three.add_member(nurse)
  with pytest.raises(Exception) as e:
    assert team_four.add_member(nurse)
  assert str(e.value) == 'Failed to add Team Member, already in maximum number of Teams'

  def test_NurseInUpToThreeTeams():
    team_one = Team()
    team_two = Team()
    team_three = Team()
    team_four = Team()
    admin_assistant = AdminAssistant(first_name = 'Jane', 
                                    last_name = 'Doe',
                                    specialities = ['Renal', 'Paediatrics'],
                                    biography = 'Lorem Ipsum')
    team_one.add_member(admin_assistant)
    team_two.add_member(admin_assistant)
    team_three.add_member(admin_assistant)
    with pytest.raises(Exception) as e:
      assert team_four.add_member(admin_assistant)
    assert str(e.value) == 'Failed to add Team Member, already in maximum number of Teams'
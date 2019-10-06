import pytest
from teamModel.models import Team, Surgeon, Nurse, AdminAssistant



class Tests:
  def setup_method(self):
      self.surgeon = Surgeon(first_name = 'John', 
                        last_name = 'Doe',
                        specialities = ['Renal', 'Paediatrics'],
                        biography = 'Lorem Ipsum')

      self.surgeon_two = Surgeon(first_name = 'Jill', 
                                 last_name = 'Doe',
                                 specialities = ['Renal', 'Paediatrics'],
                                 biography = 'Lorem Ipsum')

      self.nurse = Nurse(first_name = 'Jane', 
                    last_name = 'Doe',
                    specialities = ['Renal', 'Paediatrics'],
                    biography = 'Lorem Ipsum')

      self.admin_assistant = AdminAssistant(first_name = 'Jack', 
                                      last_name = 'Doe',
                                      specialities = ['Renal', 'Paediatrics'],
                                      biography = 'Lorem Ipsum')

  def test_TeamHasRoster(self):
    team = Team()
    assert team.roster == []

  def test_TeamCanAddMembers(self):
    team = Team()
    team.add_member(self.surgeon)
    assert team.roster == [self.surgeon]

  def test_TeamHasValidityCheck(self):
    team = Team()
    team.add_member(self.surgeon)
    assert team.validity_check() == False

  def test_OneSurgeonOneNurse(self):
    team = Team()
    team.add_member(self.surgeon)
    team.add_member(self.nurse)
    assert team.validity_check() == True

  def test_MaxOneSurgeon(self):
    team = Team()
    team.add_member(self.nurse)
    team.add_member(self.surgeon)
    team.add_member(self.surgeon_two)
    assert team.validity_check() == False

  def test_OneAdminAssistant(self):
    team = Team()
    team.add_member(self.surgeon)
    team.add_member(self.nurse)
    team.add_member(self.admin_assistant)
    assert team.validity_check() == True

  def test_MaxOneAdminAssistant(self):
    team = Team()
    team.add_member(self.surgeon)
    team.add_member(self.nurse)
    team.add_member(self.admin_assistant)
    team.add_member(self.admin_assistant)
    assert team.validity_check() == False

  def test_UnlimitedNurses(self):
    team = Team()
    team.add_member(self.surgeon)
    team.add_member(self.nurse)
    team.add_member(self.nurse)
    assert team.validity_check() == True

  def test_AddMemberAddsTeamToMembersTeamList(self):
    team = Team()
    team.add_member(self.nurse)
    assert len(self.nurse.teams) == 1

  def test_NurseInUpToThreeTeams(self):
    team_one = Team()
    team_two = Team()
    team_three = Team()
    team_four = Team()
    team_one.add_member(self.nurse)
    team_two.add_member(self.nurse)
    team_three.add_member(self.nurse)
    with pytest.raises(Exception) as e:
      assert team_four.add_member(self.nurse)
    assert str(e.value) == 'Failed to add Team Member, already in maximum number of Teams'

  def test_AdminAssistantInUpToThreeTeams(self):
    team_one = Team()
    team_two = Team()
    team_three = Team()
    team_four = Team()
    team_one.add_member(self.admin_assistant)
    team_two.add_member(self.admin_assistant)
    team_three.add_member(self.admin_assistant)
    with pytest.raises(Exception) as e:
      assert team_four.add_member(self.admin_assistant)
    assert str(e.value) == 'Failed to add Team Member, already in maximum number of Teams'

  def test_SurgeonInUpToOneTeam(self):
    team_one = Team()
    team_two = Team()
    team_one.add_member(self.surgeon)
    with pytest.raises(Exception) as e:
      assert team_two.add_member(self.surgeon)
    assert str(e.value) == 'Failed to add Team Member, already in maximum number of Teams'


from teamModel.models import TeamMember

genericTeamMember = TeamMember(firstName='John', 
                               lastName='Doe')

def test_TeamMemberHasFirstName():
  assert genericTeamMember.firstName == 'John'

def test_TeamMemberHasLastName():
  assert genericTeamMember.lastName == 'Doe'

def test_TeamMemberHasOnLeave():
  assert genericTeamMember.onLeave == False

def test_TeamMemberCanToggleOnLeave():
  genericTeamMember.toggleOnLeave()
  assert genericTeamMember.onLeave == True

def test_TeamMemberCanToggleOnLeaveBack():
  genericTeamMember.toggleOnLeave()
  assert genericTeamMember.onLeave == False
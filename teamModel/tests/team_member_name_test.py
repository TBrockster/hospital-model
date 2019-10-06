from teamModel.models import TeamMember

genericTeamMember = TeamMember(firstName='John', 
                               lastName='Doe')

def test_TeamMemberHasFirstName():
  assert genericTeamMember.firstName == 'John'

def test_TeamMemberHasLastName():
  assert genericTeamMember.lastName == 'Doe'

def test_TeamMemberHasOnLeave():
  assert genericTeamMember.onLeave == False
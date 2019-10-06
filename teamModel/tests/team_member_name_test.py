from teamModel.models import TeamMember

genericTeamMember = TeamMember('John')

def test_TeamMemberHasName():
  assert genericTeamMember.name == 'John'
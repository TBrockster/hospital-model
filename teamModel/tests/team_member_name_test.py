from teamModel.models import TeamMember

genericTeamMember = TeamMember(firstName='John', 
                               lastName='Doe',
                               type='Surgeon',
                               specialities = ['Renal', 'Paediatrics'],
                               biography='Lorem Ipsum')

def test_TeamMemberHasFirstName():
  assert genericTeamMember.firstName == 'John'

def test_TeamMemberHasLastName():
  assert genericTeamMember.lastName == 'Doe'

def test_TeamMemberHasType():
  assert genericTeamMember.type == 'Surgeon'

def test_TeamMemberHasOnLeave():
  assert genericTeamMember.onLeave == False

def test_TeamMemberCanToggleOnLeave():
  genericTeamMember.toggleOnLeave()
  assert genericTeamMember.onLeave == True

def test_TeamMemberCanToggleOnLeaveBack():
  genericTeamMember.toggleOnLeave()
  assert genericTeamMember.onLeave == False

def test_TeamMemberHasSpecialities():
  assert genericTeamMember.specialities == ['Renal', 'Paediatrics']

def test_TeamMemberHasBiography():
  assert genericTeamMember.biography == 'Lorem Ipsum'
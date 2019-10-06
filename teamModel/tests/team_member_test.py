from teamModel.models import TeamMember

genericTeamMember = TeamMember(first_name = 'John', 
                               last_name = 'Doe',
                               type = 'Surgeon',
                               specialities = ['Renal', 'Paediatrics'],
                               biography = 'Lorem Ipsum')

def test_TeamMemberHasFirstName():
  assert genericTeamMember.first_name == 'John'

def test_TeamMemberHasLastName():
  assert genericTeamMember.last_name == 'Doe'

def test_TeamMemberHasType():
  assert genericTeamMember.type == 'Surgeon'

def test_TeamMemberHasOnLeave():
  assert genericTeamMember.on_leave == False

def test_TeamMemberCanToggleOnLeave():
  genericTeamMember.toggle_on_leave()
  assert genericTeamMember.on_leave == True

def test_TeamMemberCanToggleOnLeaveBack():
  genericTeamMember.toggle_on_leave()
  assert genericTeamMember.on_leave == False

def test_TeamMemberHasSpecialities():
  assert genericTeamMember.specialities == ['Renal', 'Paediatrics']

def test_TeamMemberHasBiography():
  assert genericTeamMember.biography == 'Lorem Ipsum'
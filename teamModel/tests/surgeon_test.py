from teamModel.models import Surgeon

surgeon = Surgeon(first_name = 'Jane',
                  last_name = 'Doe',
                  specialities = ['Renal'],
                  biography = 'Hello World')

def test_SurgeonHasType():
  assert surgeon.type == 'Surgeon'
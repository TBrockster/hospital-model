from teamModel.logic import Nurse

nurse = Nurse(first_name = 'John',
                  last_name = 'Doe',
                  specialities = ['Renal'],
                  biography = 'Hello World')

def test_NurseHasType():
  assert nurse.type == 'Nurse'
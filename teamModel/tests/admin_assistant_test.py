from teamModel.logic import AdminAssistant

admin_assistant = AdminAssistant(first_name = 'John',
                                 last_name = 'Doe',
                                 specialities = ['Renal'],
                                 biography = 'Hello World')

def test_AdminAssistantHasType():
  assert admin_assistant.type == 'Admin Assistant'
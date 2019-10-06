from teamModel.models import Team

def test_TeamHasRoster():
  team = Team()
  assert team.roster == []
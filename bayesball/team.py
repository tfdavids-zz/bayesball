class Team(object):
    def __init__(self):
        self.players = []
        self.lineup = []
        self.positions = []

class TeamState(object):
    def __init__(self, team):
        self.atbat = 0

        self.players = team.players
        self.lineup = team.lineup
        self.positions = team.position

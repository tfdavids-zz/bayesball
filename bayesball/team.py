class Team(object):
    def __init__(self, players):
        self.players = players
        self.lineup = players
        self.positions = players

class TeamState(object):
    def __init__(self, team):
        self.atbat = 0

        self.players = team.players
        self.lineup = team.lineup
        self.positions = team.positions

    def getBatter(self):
        return self.lineup[self.atbat]

    def getPitcher(self):
        return self.positions[0]


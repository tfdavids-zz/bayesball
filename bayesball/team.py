POSITIONS = ['P', 'C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF']

class Team(object):
    def __init__(self, players):
        self.players = players
        self.lineup = players
        self.positions = players

    def editPositions(self, new_positions):
        """new_positions should be a list permutation of (0..8)"""
        old_positions = self.positions
        self.positions = [old_positions[i] for i in new_positions]

    def editLineup(self, new_lineup):
        """new_lineup should be a list permutation of (0..8)"""
        old_lineup = self.lineup
        self.lineup = [old_lineup[i] for i in new_lineup]

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


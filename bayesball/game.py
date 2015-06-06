import team

class Game(object):
    def __init__(self, home, away):
        self.home = home
        self.away = away

        self.homeTeamState = team.TeamState(self.home)
        self.awayTeamState = team.TeamState(self.away)

    def atBat(self):
        batter = self.homeTeamState.getBatter()
        pitcher = self.awayTeamState.getPitcher()

        outcome = self.matchup(batter, pitcher)

    def matchup(self, batter, pitcher):
        pass

import team
import random

class Game(object):
    def __init__(self, home, away):
        self.home = home
        self.away = away

        self.homeTeamState = team.TeamState(self.home)
        self.awayTeamState = team.TeamState(self.away)
        
	self.inning = 0
	self.is_top_of_inning = True
	self.outs = 0
	self.bases = [None, None, None]
 
    def atBat(self):
        batter = self.homeTeamState.getBatter()
        pitcher = self.awayTeamState.getPitcher()

        self.matchup(batter, pitcher)
        
	self.show_game_state()

    def matchup(self, batter, pitcher):
        batting_avg = batter.batting_avg
	pitching_avg = pitcher.batting_avg_against

	hit_probability = (batting_avg + pitching_avg)/2
	print "The probability of getting a hit is: ", hit_probability

	if random.random() <= hit_probability:
	    self.bases[0] = 'Batter'
	    print "The batter got a hit!"
	else:
	    self.outs += 1	
	    print "The pitcher got the out!"

    def show_game_state(self):
	if self.is_top_of_inning:
	    print "It is the top of Inning", self.inning + 1
	else:
	    print "It is the bottom of Inning", self.inning + 1
	
	print "There are", self.outs, "out(s)."
	
	if self.bases == [None, None, None]:
	    print "The bases are empty."
	else:
	    print "The runners are:", self.bases


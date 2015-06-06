import sys

from bayesball import team
from bayesball import player
from bayesball import game

print """
Welcome to Bayesball! For now, you are in charge of the Oakland Athletics, as
they take on the Colorado Rockies.
"""

print """
Setting up team . . .
"""

charlie_blackmon = player.Player()
dj_lemahieu = player.Player()
troy_tulowitzki = player.Player()
carlos_gonzalez = player.Player()
nolan_arenado = player.Player()
ben_paulsen = player.Player()
nick_hundley = player.Player()
brandon_barnes = player.Player()
eddie_butler = player.Player()

billy_burns = player.Player(name='Billy Burns')
marcus_semien = player.Player(name='Marcus Semien')
ben_zobrist = player.Player(name='Ben Zobrist')
billy_butler = player.Player(name='Billy Butler')
brett_lawrie = player.Player(name='Brett Lawrie')
josh_reddick = player.Player(name='Josh Reddick')
stephen_vogt = player.Player(name='Stephen Vogt')
eric_sogard = player.Player(name='Eric Sogard')
sonny_gray = player.Player(name='Sonny Gray')

rockies = team.Team([
    charlie_blackmon,
    dj_lemahieu,
    troy_tulowitzki,
    carlos_gonzalez,
    nolan_arenado,
    ben_paulsen,
    nick_hundley,
    brandon_barnes,
    eddie_butler
])

athletics = team.Team([
    billy_burns,
    marcus_semien,
    ben_zobrist,
    billy_butler,
    brett_lawrie,
    josh_reddick,
    stephen_vogt,
    eric_sogard,
    sonny_gray
])

print """
Teams successfully set up!
"""

print """
Select an option:
[1] Edit your lineup
[2] Play game
"""

def editLineup():
    print """
    Here is your lineup:
    """

    positions = ['P', 'C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF']

    for i in xrange(9):
        print '%d. %s (%s)' % (i+1, athletics.players[i].name, positions[i])

def beginGame():
    print """
    Starting game . . .
    """
    
    my_game = game.Game(rockies, athletics)
    
    print """
    Started game!
    """
    
    my_game.atBat()

choice = raw_input()
if choice == '1':
    editLineup()
elif choice == '2':
    beginGame()
else:
    raise Exception("did not choose valid option")


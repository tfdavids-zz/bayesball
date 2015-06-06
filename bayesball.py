import sys

from bayesball import team as team_model
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

rockies = team_model.Team([
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

athletics = team_model.Team([
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

def editLineup(team):
    new_lineup = range(9)
    print """
    Enter a number to move that player
    """
    choice = int(raw_input()) - 1
    player = team.lineup[new_lineup[choice]]
    new_lineup[choice] = -1

    while -1 in new_lineup:
        print "Select a position for %s" % player.name
        for i, x in enumerate(new_lineup):
            print "%s. %s" % (i+1, "<empty>" if x == -1 else team.lineup[x].name)
        new_choice = int(raw_input()) - 1
        player = team.lineup[new_lineup[new_choice]]
        new_lineup[new_choice] = choice
        choice = new_choice

    team.editLineup(new_lineup)

def editPositions(team):
    new_positions = range(9)
    print """
    Enter a number to move that player
    """
    choice = int(raw_input()) - 1
    player = team.positions[new_positions[choice]]
    new_positions[choice] = -1

    while -1 in new_positions:
        print "Select a position for %s" % player.name
        for i, x in enumerate(new_positions):
            print "%s. %s" % (team_model.POSITIONS[i], "<empty>" if x == -1 else team.positions[x].name)
        new_choice = int(raw_input()) - 1
        player = team.positions[new_positions[new_choice]]
        new_positions[new_choice] = choice
        choice = new_choice

    team.editPositions(new_positions)

def editRoster():
    while True:
        print """
        Here is your lineup:
        """

        for i in xrange(9):
            position = athletics.positions.index(athletics.lineup[i])
            print '%d. %s (%s)' % (i+1, athletics.lineup[i].name, team_model.POSITIONS[position])

        print """
        Select an option:
        [1] Edit positions
        [2] Edit lineup
        [3] Play game
        """

        choice = raw_input()
        if choice == '1':
            editPositions(athletics)
        elif choice == '2':
            editLineup(athletics)
        elif choice == '3':
            break

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
    editRoster()
    beginGame()
elif choice == '2':
    beginGame()
else:
    raise Exception("did not choose valid option")


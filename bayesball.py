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

billy_burns = player.Player()
marcus_semien = player.Player()
ben_zobrist = player.Player()
billy_butler = player.Player()
brett_lawrie = player.Player()
josh_reddick = player.Player()
stephen_vogt = player.Player()
eric_sogard = player.Player()
sonny_gray = player.Player()

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

my_game = game.Game(rockies, athletics)

print """
Started game!
"""

my_game.atBat()

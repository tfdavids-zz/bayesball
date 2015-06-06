class Player(object):
    def __init__(self, position=None, name=None):
        self.position = position
        self.name = name
        # ...

        self.batting_avg = 0.333
        self.batting_avg_against = 0.300

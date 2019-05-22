


import collections

# 11. Team photo day 1



class Team:
    Player = collections.namedtuple('Player', ('height'))

    def __init__(self, height):
        self._players = [Team.Player(h) for h in height]


    # checks if team0 can be placed in front of team1.
    @staticmethod
    def valid_placement_exists(team0, team1):
        return all(a < b for a, b in zip(sorted(team0._players), sorted(team1._players)))


tt=Team

team_0 = [
    tt.Player(height=1),
    tt.Player(height=2),
    tt.Player(height=3),
    tt.Player(height=4),
    tt.Player(height=5)
]

team_1 = [
    tt.Player(height=2),
    tt.Player(height=3),
    tt.Player(height=4),
    tt.Player(height=5),
    tt.Player(height=6)
]

t0 = Team(team_0)
t1 = Team(team_1)

print(tt.valid_placement_exists(t0, t1))

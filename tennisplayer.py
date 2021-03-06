#tennisplayer.py
#modified player.py from class
from random import *

class Player:
    def __init__(self, prob):
        self.prob = prob
        self.score = 0

    def winsServe(self):
        # Returns true with probability self.prob
        return random() <= self.prob

    def incScore(self):
        # Add a point to this player's score
        if self.score == 0:
            self.score = self.score + 15
        if self.score == 15:
            self.score = self.score + 15
        if self.score ==30:
            self.score = self.score + 10
        if self.score == 40:
            self.score = self.score + 10

    def getScore(self):
        # Return this player's current score
        return self.score

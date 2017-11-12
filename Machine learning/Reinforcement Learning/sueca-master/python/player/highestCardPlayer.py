from player.player import Player
from operator import attrgetter

class HighestCardPlayer(Player):
    def __init__(self,id, cards):
        Player.__init__(self,id,cards)


    def chooseCard(self, possibleCards):
        return max(possibleCards, key=attrgetter('value'))
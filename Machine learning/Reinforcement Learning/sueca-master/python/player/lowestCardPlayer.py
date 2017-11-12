from player.player import Player
from operator import attrgetter

class LowestCardPlayer(Player):
    def __init__(self,id, cards):
        Player.__init__(self,id,cards)


    def chooseCard(self, possibleCards):
        return min(possibleCards, key=attrgetter('value'))
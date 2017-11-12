from player.player import Player
import random as rnd


class RandomPlayer(Player):
    def __init__(self,id, cards):
        Player.__init__(self, id, cards)

    def chooseCard(self,possibleCards):
        card = rnd.choice(possibleCards)
        return card

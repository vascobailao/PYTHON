from player.player import Player
from operator import attrgetter



class MinimaxPlayer(Player):

    def __init__(self, id, cards):
        Player.__init__(self, id, cards)

    def chooseCard(self, possibleCards):
        aux = []
        if(possibleCards[0]!= False):
            cardPlayed = possibleCards[0]
            for card in possibleCards[1]:
             if(card.getValue() >= cardPlayed.getValue()):
                 aux.append(card)
            if(len(aux)==0):
                card = min(possibleCards[1], key=attrgetter('value'))
            else:
                card = min(aux, key=attrgetter('value'))
        else:
            card = max(possibleCards[1], key=attrgetter('value'))

        return card

    def possibleCards(self, cardsPlayedInturn):
        retList = []
        aux = []
        if(len(cardsPlayedInturn) > 0):
            for card in self.cards:
                if(cardsPlayedInturn[0].getNaipe() == card.getNaipe()):
                    aux.append(card)
            retList = [cardsPlayedInturn[0], aux]
            if (len(aux)==0):
                aux = self.cards
                retList = [False, aux]
        else:
            aux = self.cards
            retList = [False, aux]
        return retList
import random as rnd
import numpy as np


class Player:

    def __init__(self, id, cards):
        self.id = id
        self.cards = cards
        # initial beliefs
        self.beliefs = np.full((10, 4), 1/37)
        self.points = 0

    def possibleCards(self, cardsPlayedInturn):
        aux = []
        if(len(cardsPlayedInturn) > 0):
            for card in self.cards:
                if(cardsPlayedInturn[0].getNaipe() == card.getNaipe()):
                    aux.append(card)
            if (len(aux)==0):
                aux = self.cards
        else:
            aux = self.cards
        return aux

    def chooseCard(self,possibleCards):
        card = rnd.choice(possibleCards)
        return card

    # pegar carta do baralho
    def pickCard(self,card):
        self.cards.append(card)
        return

    def playCard(self, card):
        self.cards.remove(card)
        return

    def getPlayerId(self):
        return self.id

    def getPlayerCards(self):
        return self.cards

    def updatePoints(self,points):
        self.points = self.points + points

    def printCards(self):
        list = []
        print(self.id)
        for card in self.cards:
            list.append("[(" + str(card.getId()) +  ") " + str(card.getName()) + " " + str(card.getNaipe()) + " ]")
        print (list)
        print()


    def playerLoop(self, cardsPlayedInTurn, game):
        possibleCards = self.possibleCards(cardsPlayedInTurn)
        card = self.chooseCard(possibleCards)
        ##print(self.getPlayerId(), card.getName(), card.getNaipe())
        game.cardsPlayedInTurn.append(card)
        self.playCard(card)
        if(len(game.baralho)>0):
            self.pickCard(game.baralho[0])
            del game.baralho[0]
        return card



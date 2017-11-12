from player.player import Player
import numpy as np


class NFQPlayer(Player):

    beliefs = []
    currentCards = []

    def __init__(self, id, cards, nrCards):
        Player.__init__(self, id, cards)
        self.beliefs = np.ones(nrCards)/nrCards
        self.currentCards = np.zeros(nrCards)
        self.initNFQ()

    def initNFQ(self):
        for card in self.cards:
            self.updateCards1(card)
        for card in self.cards:
            self.updateBeliefs0(card)

    def updateProb(self):
        nrCards = np.sum(self.beliefs!=0)
        if(nrCards>0):
            self.beliefs[self.beliefs!=0] = 1/nrCards

    def updateCards1(self, card):
        self.currentCards[card.getId()] = 1

    def updateCards0(self, card):
        self.currentCards[card.getId()] = 0

    def updateBeliefs0(self, card):
        self.beliefs[card.getId()] = 0
        self.updateProb()

    def printState(self):
        print(self.currentCards)
        print(self.beliefs)

    def reviewTurn(self,card):
        self.updateBeliefs0(card)

    def pickCard(self,card):
        self.cards.append(card)
        self.updateCards1(card)
        self.updateBeliefs0(card)
        return

    def playCard(self, card):
        self.cards.remove(card)
        self.updateCards0(card)
        self.updateBeliefs0(card)
        return

    def playerLoop(self, cardsPlayedInTurn, game):
        possibleCards = self.possibleCards(cardsPlayedInTurn)
        if(len(cardsPlayedInTurn)>0):
            self.updateBeliefs0(cardsPlayedInTurn[0])
        card = self.chooseCard(possibleCards)
        ##print(self.getPlayerId(), card.getName(), card.getNaipe())
        game.cardsPlayedInTurn.append(card)
        self.playCard(card)
        if(len(game.baralho)>0):
            self.pickCard(game.baralho[0])
            del game.baralho[0]
        return card


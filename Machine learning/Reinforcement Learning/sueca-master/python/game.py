from random import shuffle
import random as rnd
from utils import parseCSV
from card import Card
from player.player import Player
from player.minimaxPlayer import MinimaxPlayer
from player.randomPlayer import RandomPlayer
from player.lowestCardPlayer import LowestCardPlayer
from player.highestCardPlayer import HighestCardPlayer
from player.nfqPlayer import NFQPlayer
from player.nfqAgent import NFQAgent
from logs.log import Log


class Game:

    firstPlayer = ""
    trumpCard = ""
    cardsPlayed = []
    cardsPlayedInTurn = []
    players = dict({})
    gamePoints = 0

    def __init__(self, logging=0):
        self.baralho = []
        self.logging = logging

    def init(self):
        self.initDeck()
        self.pickTrumpCard()
        self.shuffleDeck()
        self.pickFirstPlayer()
        return

    def closeTurn(self, cardsPlayedInTurn):
        self.cardsPlayed.extend(cardsPlayedInTurn)
        self.cardsPlayedInTurn = []

    def initDeck(self):
        self.baralho = parseCSV('csv/cards.csv')

    def shuffleDeck(self):
        shuffle(self.baralho)

    def pickTrumpCard(self):
        self.trumpCard = rnd.choice(self.baralho)

    def pickFirstPlayer(self):
        self.firstPlayer = rnd.randint(0,2)

    def pointsPerTurn(self):
        card1 = self.cardsPlayedInTurn[0]
        card2 = self.cardsPlayedInTurn[1]
        points = card1.getValue() + card2.getValue()
        return points

    def winner(self, id1, card1, id2, card2):
        if(card1.getNaipe() == card2.getNaipe()):
            if(card1.getValue() > card2.getValue()):
                return id1
            elif(card1.getValue() == card2.getValue()):
                if(int(card1.getName())>int(card2.getName())):
                    return id1
                else:
                    return id2
            else:
                return id2
        elif(card1.getNaipe() == self.trumpCard.getNaipe() and card2.getNaipe() != self.trumpCard.getNaipe()):
            return id1
        elif(card2.getNaipe() == self.trumpCard.getNaipe() and card1.getNaipe() != self.trumpCard.getNaipe()):
            return id2
        elif(card2.getNaipe() != self.trumpCard.getNaipe() and card2.getNaipe() != card1.getNaipe()):
            return id1
        else:
            raise ValueError("Failed to find winner")

    def log(self):
        # log de jogadas
        return

    @staticmethod
    def getCardsPlayedInTurn(self):
        return self.cardsPlayedInTurn

    def gameLoop(self):
        log = Log("logs/logfiles/")
        #incializacoes de jogo e alteracoes no objecto game
        loops = 20
        self.init()
        ##print("Trump:", self.trumpCard.getNaipe(), "\n")
        firstPlayer = NFQAgent("NFQAgent", self.baralho[:3],40)
        secondPlayer = MinimaxPlayer("MinimaxPlayer", self.baralho[3:6])
        ##firstPlayer.printCards()
        ##secondPlayer.printCards()
        del self.baralho[:6]
        i = 0
        for i in range (loops):
            ##print("Loop: ", i)
            self.players = {firstPlayer.getPlayerId(): firstPlayer, secondPlayer.getPlayerId(): secondPlayer}
            firstPlayer.playerLoop(self.cardsPlayedInTurn, self)
            secondPlayer.playerLoop(self.cardsPlayedInTurn, self)
            winner = self.winner(firstPlayer.getPlayerId(),self.cardsPlayedInTurn[0],secondPlayer.getPlayerId() ,self.cardsPlayedInTurn[1])
            if(firstPlayer.getPlayerId() == "NFQAgent"):
                firstPlayer.reviewTurn(self.cardsPlayedInTurn[1])
                ##firstPlayer.printState()
            ##else:
                ##secondPlayer.printState()
            ##print("")
            ##print("Winner:", winner)
            points = self.pointsPerTurn()
            ##print("Points:",points, "\n")

            beliefsLOG = []
            cardsLOG = []
            pointsLOG = 0
            if(self.logging == 1):

                if(firstPlayer.getPlayerId()=="NFQAgent"):
                    if(winner == firstPlayer.getPlayerId()):
                        pointsLOG = self.pointsPerTurn()
                    else:
                        pointsLOG = -self.pointsPerTurn()
                    beliefsLOG = firstPlayer.beliefs
                    cardsLOG = firstPlayer.currentCards
                else:
                    if(winner == secondPlayer.getPlayerId()):
                        pointsLOG = self.pointsPerTurn()
                    else:
                        pointsLOG = -self.pointsPerTurn()
                    beliefsLOG = secondPlayer.beliefs
                    cardsLOG = secondPlayer.currentCards


                #log
                log.writeLogNP(beliefsLOG, cardsLOG,pointsLOG)


            self.closeTurn(self.cardsPlayedInTurn)
            firstPlayer = self.players.pop(winner)
            firstPlayer.updatePoints(points)
            secondPlayer = list(self.players.values())[0]

        log.closeLog()
        ##print(firstPlayer.getPlayerId(), firstPlayer.points, secondPlayer.getPlayerId(), secondPlayer.points)

        if(firstPlayer.points > secondPlayer.points):
            return firstPlayer
        else:
            return secondPlayer


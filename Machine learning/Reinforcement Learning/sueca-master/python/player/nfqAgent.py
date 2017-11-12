from player.nfqPlayer import NFQPlayer
from nn.pyBrainNN import NeuralNetwork
import numpy as np
import utils

class NFQAgent(NFQPlayer):

    def __init__(self,id, cards, nrCards=40):
        self.fullDeck = utils.parseCSV()
        self.network = NeuralNetwork()
        NFQPlayer.__init__(self, id, cards, nrCards)


    def auxDeck(self, beliefs):
        #print(beliefs)
        auxD = list(self.fullDeck)
        i=0
        for val in beliefs:
            if(val==0):
                for card in auxD:
                    if card.getId() == i:
                        auxD.remove(card)
                        #print("REMOVE: ", card.getId())
            i = i + 1
        #print(len(auxD))

        return auxD



    def chooseCard(self,possibleCards):
        qlist = []
        ##print("POSSSIBLE CARDS:", possibleCards)
        if(len(possibleCards)>1):
            for card in possibleCards:
                medQValues = self.generate(card)
                qlist.append(medQValues)
            index = qlist.index(max(qlist))
            card = possibleCards[index]
        else:
            card = possibleCards[0]
        #for card in possibleCards:
        #    print(card.getId())
        #print(qlist)
        return card


    #inpt = tuple(np.append(belief, cards))
    def generate(self, card):
        qValues = []
        curr = np.array(self.currentCards)
        bel = np.array(self.beliefs)
        auxDeck = np.array(self.auxDeck(bel))

        #print("Card: " + str(card.getId()))
        for bcard in auxDeck:
            #print("Beliefs Estado Atual:", self.beliefs)
            #print("Cartas Estado Atual:", self.currentCards)
            #print("bCard: " + str(bcard.getId()))

            curr = self.updCards0(curr, card)


            curr = self.updCards1(curr, bcard)
            bel = self.updBeliefs0(bel, bcard)
            #print("Beliefs Proximo Estado", bel)
            #print("Cartas Proximo Estado", curr)
            input = np.append(curr,bel)
            #print(input)
            qValue = self.network.test(input)
            qValues.append(qValue)


            curr = np.array(self.currentCards)
            bel = np.array(self.beliefs)

        #print("QVaulues: ",qValues)
        #print("Nr Cartas Baralho: ", len(baralho))
        #print("Nr Qvalues: ", len(qValues))

        if(len(qValues)>0):
            media = sum(qValues)/len(qValues)
        else:
            media = 0
            print(...)
        return media



    def updCards0(self, currCards, card):
        curr = currCards
        curr[card.getId()] = 0
        return curr

    def updCards1(self, currCards, card):
        curr = currCards
        curr[card.getId()]=1
        return curr

    def updBeliefs0(self, beliefs, card):
        bel = beliefs
        bel[card.getId()] = 0
        bel = self.updProb(bel)
        return bel

    def updProb(self, beliefs):
        bel = beliefs
        nrCards = np.sum(bel!=0)
        if(nrCards>0):
            bel[bel!=0] = 1/nrCards
        return bel

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.customxml.networkwriter import NetworkWriter
from pybrain.tools.customxml.networkreader import NetworkReader
from pybrain.supervised.trainers import RPropMinusTrainer
from logs.log import Log
import numpy as np
import os.path

class NeuralNetwork:

    def __init__(self,df=0.9):
        self.inputSize = 80
        self.hiddenSize = 100
        self.outputSize = 1
        self.df = df

        if (os.path.isfile("nn/neural-network.xml")):
            ##print("Loading Network from file")
            self.net = NetworkReader.readFrom('nn/neural-network.xml')
            self.ds = SupervisedDataSet(self.inputSize, self.outputSize)
            self.loadDataSet()
            self.trainer = BackpropTrainer(self.net, self.ds)
        else:
            print("Building Network")
            self.net = buildNetwork(self.inputSize,self.hiddenSize,self.outputSize, bias=True)
            self.ds = SupervisedDataSet(self.inputSize, self.outputSize)
            self.loadDataSet()
            self.trainer = BackpropTrainer(self.net, self.ds)
            self.train()
            self.saveNet()



    def loadDataSet(self):

        l = Log("logs/logfiles/")

        for fic in range(l.getLatestLogNr()):
            line = l.readLogNP(fic)
            for x in range (len(line)):
                belief = line[x][0]
                cards = line[x][1]
                reward = (line[x][2]+22)/44

                inpt = tuple(np.append(belief, cards))

                try:
                    belief2 = line[x + 1][0]
                    cards2 = line[x + 1][1]
                    output2 = self.test(tuple(np.append(belief2,cards2)))
                    target = tuple(reward + self.df*output2)
                except:
                    target = tuple(reward)

                self.ds.addSample(inpt,target)

    def train(self):

        print("training netwok")

        #self.trainer.trainUntilConvergence(maxEpochs=10)
        self.trainer.train()

        print("trained")

    def trainFromFile(self):
        error = self.trainer.train()
        print("error:", error)
        self.saveNet()
        return error

    def test(self, input):

        return self.net.activate(input)

    def saveNet(self):
        print("Net Saved")
        NetworkWriter.writeToFile(self.net, 'nn/neural-network.xml')


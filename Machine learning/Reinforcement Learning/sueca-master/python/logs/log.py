import numpy as np
import csv
import os


class Log:
    logNr = 0
    logPath = "logfiles/"
    #format = "log-*.csv"

    def __init__(self, path="logfiles/"):
        self.logPath = path
        self.logNr = self.getLatestLogNr() + 1

    # vai buscar o nr do log mais recente na pasta logfiles
    def getLatestLogNr(self):
        flist = [each for each in os.listdir(self.logPath) if each.startswith("log-") and each.endswith(".csv")]
        ##print(flist)
        if(flist != []):
            return len(flist) - 1
        else:
            return -1

    #escreve uma linha no log atual (identificado pelo logNr)
    def writeLogNP(self, beliefs, cards, reward): #[[cards],[beliefs]]
        array = [np.array_str(cards),np.array_str(beliefs), reward]
        logname = "log-" + str(self.logNr) +".csv"
        ##print(logname)
        with open(self.logPath + logname, "a", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(array)
        return logname

    # le um log inteiro identificado por logNr e retorna uma lista em que cada entrada tem o formato
    # [npArray->stringCards, npArray->stringBeliefs]
    # cada entrada é um np Array
    def readLogNP(self, logNr):
        logArray = []
        logname = "log-" + str(logNr) + ".csv"
        ##print(logname)
        with open(self.logPath + logname, "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                belief = np.fromstring(row[0].replace("[","").replace("]",""),dtype=float, sep=' ')
                cards = np.fromstring(row[1].replace("[","").replace("]",""),dtype=float, sep=' ')
                reward = np.fromstring(row[2].replace("[","").replace("]",""),dtype=float, sep=' ')
                logArray.append([belief, cards, reward])
        return logArray

    #esta funçao deve ser chamada ao fim de cada jogo para incrementar o valor do log
    def closeLog(self):
        self.logNr = self.logNr + 1

    #vai buscar o valor atual do log
    def getCurrentLog(self):
        return self.logNr

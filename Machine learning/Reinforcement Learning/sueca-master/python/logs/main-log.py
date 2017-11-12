import numpy as np
from logs.log import Log

l = Log()

def testWrite():
    i=0
    for i in range(10):
       j=0
       for j in range(3):
           l.writeLogNP(np.array([i,j]),np.array([i,j]),np.array([j]))
       j=0
       l.closeLog() #ao chamar este metodo é escrito um novo ficheiro de log  na proxima iteracao



def testRead():
    for i in range(l.getLatestLogNr()):
        print("Log " + str(i) + " : " + str(l.readLogNP(i))) # le cada row do ficheiro para uma entrada na lista

testWrite()
testRead()
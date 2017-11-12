
from game import Game
from nn.pyBrainNN import NeuralNetwork
import csv

i = 0
j = 0
w = 0
games = 50
nnet = NeuralNetwork()
##for j in range(35):
for j in range(100):
    for i in range(games):
        gm = Game(0)
        winner = gm.gameLoop()
        if(winner.getPlayerId()== "NFQAgent"):
            w = w + 1
    print("Train iteration: ", j + 1)
    print("Win Ratio:", w/games, "\nWin:", w, "Loss:", games - w)
    error = nnet.trainFromFile()
    with open("Results/ErrorsStatus.csv", "a") as myfile:
        writer = csv.writer(myfile, delimiter=',')
        writer.writerow([j + 1,w,games-w,w/games,error])
    w = 0
print(w)

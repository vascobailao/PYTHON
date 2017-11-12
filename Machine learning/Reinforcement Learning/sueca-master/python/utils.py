#!/usr/bin/python
import csv
from card import Card





def parseCSV(filename="csv/cards.csv"):
    cards = []
    with open(filename, "r") as csvfile:
         reader = csv.reader(csvfile, delimiter=';', quotechar='|')
         cardId = 0
         for row in reader:
             card = Card(cardId, row[0],row[1],int(row[2]))
             cards.append(card)
             cardId = cardId + 1
    return cards


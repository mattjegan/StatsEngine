#!/usr/bin/python

import Season
import Team
import Player

import cPickle as pickle

from os import listdir
from os.path import isfile, join

class StatsEngine:
    def __init__(self):
        self.seasons = []
        self.players = []

        ## Load all players
        filesInRoot = [f for f in listdir(".") if isfile(join(".", f))]
        for fileName in filesInRoot:
            if fileName[-4:] == ".pla":
                self.players.append(pickle.load(open(fileName, "rb")))

    def addPlayer(self, player):
        self.players.append(player)

    def saveAll(self):
        for player in self.players:
            pickle.dump(player, open(player.getFileName(), "wb"))

    def showPlayers(self):
        if len(self.players) == 0: print "Empty"
        for player in self.players:
            print player.getName()

def main():
    eng = StatsEngine()
    eng.showPlayers()
    #matt = Player.Player("Matt", "Egan", 80, "Ass", 43, 7)
    #eng.addPlayer(matt)
    #eng.saveAll()

if __name__ == "__main__": main()

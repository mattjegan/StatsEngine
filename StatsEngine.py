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
        filesInRoot = [f for f in listdir("./players") if isfile(join("./players", f))]
        for fileName in filesInRoot:
            if fileName[-4:] == ".pla":
                self.players.append(pickle.load(open("./players/" + fileName, "rb")))

    def addPlayer(self, player):
        if self.playerDoesNotExist(player):
            self.players.append(player)
            print "Added player"
        else:
            print "Player already exists"

    def playerDoesNotExist(self, player):
        for p in self.players:
            if p.getIDnum() == player.getIDnum():
                return False
        return True

    def saveAll(self):
        ## Pickle all player instances
        for player in self.players:
            pickle.dump(player, open(player.getFileName(), "wb"))

    def showPlayers(self):
        if len(self.players) == 0: print "Empty"
        for player in self.players:
            print player.getName()

    def deletePlayer(self, player):
        self.players.remove(player)

    def getPlayers(self):
        return self.players

def main():
    eng = StatsEngine()

    eng.getPlayers()[0].displayAllStats()
    eng.getPlayers()[0].addGoal()

    eng.saveAll()
    eng.showPlayers()

if __name__ == "__main__": main()

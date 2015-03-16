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
        ## Delete all players first
        #filesInRoot = [f for f in listdir(".") if isfile(join(".", f))]
        #for fileName in filesInRoot:
        #    if fileName[-4:] == ".pla":
        #        self.players.append(pickle.load(open(fileName, "rb")))

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
    #for player in eng.getPlayers():
    #    eng.deletePlayer(player)
    matt = Player.Player("Matt", "Egan", 80, "ASA", 15, 15)
    eng.addPlayer(matt)
    eng.saveAll()

if __name__ == "__main__": main()

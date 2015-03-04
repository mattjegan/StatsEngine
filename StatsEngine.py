#!/usr/bin/python

import Season
import Team
import Player

import cPickle as pickle

import os
import sys

class StatsEngine:
    def __init__(self):
        self.seasons = []
        self.players = []

        ## Load all players
        rootDir = #Insert code for getting the root directory here
        for fileName in rootDir:
            if fileName[-3:] == ".pla":
                self.players.append(pickle.load(open(fileName, "rb")))

    def addPlayer(self, player):
        self.players.append(player)

    def saveAll(self):
        for player in self.players:
            pickle.dump(player, open(player.getFileName(), "wb"))

def main():
    pass

if __name__ == "__main__": main()

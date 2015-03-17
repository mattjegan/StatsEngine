#!/usr/bin/python

import Season
import Team
import Player
import Game

import datetime

import cPickle as pickle

from os import listdir
from os.path import isfile, join

class StatsEngine:
    def __init__(self):
        self.seasons = []
        self.players = []
        self.teams = []

        ## Load all players
        filesInRoot = [f for f in listdir("./players") if isfile(join("./players", f))]
        for fileName in filesInRoot:
            if fileName[-4:] == ".pla":
                self.players.append(pickle.load(open("./players/" + fileName, "rb")))

        ## Load teams
        teamFile = open("./rsc/teams.txt", "rb")
        self.teams = [t.strip() for t in teamFile]
        if '' in self.teams:
            self.teams.remove('')
        teamFile.close()

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

        ## Save team names
        teamFile = open("./rsc/teams.txt", "wb")
        for t in self.teams:
            teamFile.write(t + "\n")
        teamFile.close()

    def showPlayers(self):
        if len(self.players) == 0: print "Empty"
        for player in self.players:
            print player.getName()

    def deletePlayer(self, player):
        self.players.remove(player)

    def getPlayers(self):
        return self.players

    def addTeam(self, teamName):
        if teamName not in self.teams:
            self.teams.append(teamName)
        else:
            print "Team already exists"

    def deleteTeam(self, teamName):
        self.teams.remove(teamName)

    def showTeams(self):
        if len(self.teams) == 0: print "Empty"
        for t in self.teams: 
            print t

    def showTeamLists(self):
        for team in self.teams:
            print team + ":"
            for player in self.players:
                if player.getTeamName() == team:
                    print "\t" + player.getName()

    def newGame(self, team1, team2):
        team1players = []
        team2players = []
        for player in self.players:
            if player.getTeamName() == team1:
                team1players.append(player)
            elif player.getTeamName() == team2:
                team2players.append(player)
        currentDate = datetime.datetime.today()
        return Game.Game(team1, team1players, team2, team2players, currentDate)

def main():
    eng = StatsEngine()

    eng.addTeam("Assassins")
    eng.addTeam("Wolves")

    eng.addPlayer(Player.Player("Matthew", "Egan", 80, "Assassins", 15, 15))
    eng.addPlayer(Player.Player("Alex", "MacKenzie", 55, "Assassins", 15, 15))

    eng.saveAll()
    eng.showPlayers()
    print
    eng.showTeams()
    print
    eng.showTeamLists()

if __name__ == "__main__": main()

#!/usr/bin/python

class Game:
    def __init__(self, team1, team1players, team2, team2players, date):
        self.team1 = team1
        self.team1players = team1players
        self.team2 = team2
        self.team2players = team2players
        self.date = date

        self.team1Score = 0
        self.team2Score = 0

    def getScore(self):
        return self.team1 + ": " + str(self.team1Score) + " - " + str(self.team2Score) + " :" + self.team2

    def addGoal(self, team):
        # Add goal to score
        if team == self.team1: 
            self.team1Score += 1
        elif team == self.team2: 
            self.team2Score += 1

    def getTeam1Players(self): 
        return self.team1players
    def getTeam2Players(self): 
        return self.team2players
    def getTeam1(self): 
        return self.team1
    def getTeam2(self): 
        return self.team2

    def getGameFile(self):
        return self.team1 + "_" + self.team2 + "_" + str(self.date)
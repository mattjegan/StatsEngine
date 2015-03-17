#!/usr/bin/python

## A record for each season a "Player" is involved in

class SeasonRecord:
    def __init__(self, year, teamName, goals, assists):
        self.year = year
        self.teamName = teamName
        self.goals = goals
        self.assists = assists
        self.points = self.goals + self.assists
    def getYear(self): return self.year
    def getTeamName(self): return self.teamName
    def getGoals(self): return self.goals
    def getAssists(self): return self.assists
    def getPoints(self): return self.points
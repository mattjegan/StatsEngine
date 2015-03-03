#!/usr/bin/python

class Player:
    def __init__(self, firstName, lastName, jerseyNumber, goalsAllTime, assistsAllTime):
        self.firstName = firstName
        self.lastName = lastName
        self.fullName = self.firstName + " " + self.lastName
        self.jerseyNumber = jerseyNumber
        
        self.goalsThisSeason = 0
        self.goalsAllTime = goalsAllTime

        self.assistsThisSeason = 0
        self.assistsAllTime = assistsAllTime

        self.pointsThisSeason = self.goalsThisSeason + self.assistsThisSeason
        self.pointsAllTime = goalsAllTime + assistsAllTime
    
    ## Getters
    def getFirstName(self): return self.firstName
    def getLastName(self): return self.lastName
    def getName(self): return self.fullName
    def getNumber(self): return self.jerseyNumber
    def getGoalsThisSeason(self): return self.goalsThisSeason
    def getGoalsAllTime(self): return self.goalsAllTime
    def getAssistsThisSeason(self): return self.assistsThisSeason
    def getAssistsAllTime(self): return self.assistsAllTime
    def getPointsThisSeason(self): return self.pointsThisSeason
    def getPointsAllTime(self): return self.pointsAllTime

    ## Setters
    def addGoal(self):
        self.goalsThisSeason += 1
        self.goalsAllTime += 1
        self.updatePoints()
    def addAssist(self):
        self.assistsThisSeason += 1
        self.assistsAllTime += 1
        self.updatePoints()
    def updatePoints(self):
        self.pointsThisSeason = self.goalsThisSeason + self.assistsThisSeason
        self.pointsAllTime = self.goalsAllTime + self.assistsAllTime
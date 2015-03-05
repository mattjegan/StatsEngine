#!/usr/bin/python

import SeasonRecord
import hashlib

class Player:
    def __init__(self, firstName, lastName, jerseyNumber, teamName, goalsAllTime, assistsAllTime):

        self.firstName = firstName
        self.lastName = lastName
        self.fullName = self.firstName + " " + self.lastName

        #self.IDnum = str(hashlib.md5().update(self.fullName).hexdigest())

        self.jerseyNumber = jerseyNumber
        self.teamName = teamName
        
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
    #def getIDnum(self): return self.IDnum
    def getNumber(self): return self.jerseyNumber
    def getTeamName(self): return self.teamName
    def getGoalsThisSeason(self): return self.goalsThisSeason
    def getGoalsAllTime(self): return self.goalsAllTime
    def getAssistsThisSeason(self): return self.assistsThisSeason
    def getAssistsAllTime(self): return self.assistsAllTime
    def getPointsThisSeason(self): return self.pointsThisSeason
    def getPointsAllTime(self): return self.pointsAllTime
    def displayAllStats(self):
        print "#--------------#"
        print self.fullName, "(", self.jerseyNumber, ")"
        print "Season Goals    :", self.goalsThisSeason
        print "All Time Goals  :", self.goalsAllTime
        print "Season Assists  :", self.assistsThisSeason
        print "All Time Assists:", self.assistsAllTime
        print "Season Points   :", self.pointsThisSeason
        print "All Time Points :", self.pointsAllTime
        print "#--------------#"

    def getFileName(self): return self.fullName + ".pla"

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

def main():
    p = Player("Matt", "Egan", 80, 43, 7)
    p.displayAllStats()
    p.addGoal()
    p.displayAllStats()
    p.addAssist()
    p.displayAllStats()


if __name__ == "__main__": main()
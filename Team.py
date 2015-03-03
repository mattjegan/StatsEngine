#!/usr/bin/python

import Player

class Team:
    def __init__(self, teamName):
        self.teamName = teamName
        self.players = []
    def addPlayer(self, player):
        self.players.append(player)
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 12:57:19 2023

@author: wwf
"""

class Dice:
    def __init__(self):
        self.top = 1
        self.bottom = 6
        self.north = 2
        self.south = 5
        self.east = 4
        self.west = 3

    def rotate(self, command):
        if command == "north":
            self.top, self.north, self.bottom, self.south = (
                self.south,
                self.top,
                self.north,
                self.bottom,
            )
        elif command == "south":
            self.top, self.north, self.bottom, self.south = (
                self.north,
                self.bottom,
                self.south,
                self.top,
            )
        elif command == "west":
            self.top, self.west, self.bottom, self.east = (
                self.east,
                self.top,
                self.west,
                self.bottom,
            )
        elif command == "east":
            self.top, self.west, self.bottom, self.east = (
                self.west,
                self.bottom,
                self.east,
                self.top,
            )


while True:
    command_number = int(input())
    if command_number == 0:
        break

    dice = Dice()
    for _ in range(command_number):
        command = input()
        dice.rotate(command)

    print(dice.top)
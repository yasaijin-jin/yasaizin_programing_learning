#!/usr/bin python3
# -*- coding: utf-8 -*-

from Study.CreateRandMaze.RandMaze import RandMaze


class Field(RandMaze):
    __field = None
    __conf = None

    def __init__(self, conf):
        super().__init__(100, 100)
        self.createMaze()
        self.__conf = conf
        self.__create_field(self.__conf.getMapData(1))

    def __create_field(self, field=None):
        import json
        self.__field = [[" " if split_field == 0 else "□" if split_field == 2 else "■"
                         for split_field in list_row] for list_row in json.loads(field)]
        del json

    def getField(self):
        return self.__field

    def setHero(self, hero):
        self.__field[hero[0]][hero[1]] = "●"

    def setMonster(self, monster=None):
        if monster:
            self.__field[monster[0]][monster[1]] = "★"

    def clear(self):
        self.__create_field(self.__conf.getMapData(1))



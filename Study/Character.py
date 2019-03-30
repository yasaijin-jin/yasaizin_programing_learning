#!/usr/bin python3
# -*- coding = utf-8 -*-


class Character(object):
    
    __hp = None
    __ap = None
    __dp = None
    __hero = None
    
    def __init__(self, conf):
        """
        勇者の初期値を設定
        """
        self.__hp = 100
        self.__ap = 5
        self.__dp = 5

        self.__hero = [0, 0]

    def getHero(self):
        return self.__hero

    def getAttack(self) -> int:
        """
        攻撃を与える
        :return:
        """
        return self.__ap

    def move(self, direction, act):
        if direction == "a":
            self.__hero[1] -= act
        if direction == "d":
            self.__hero[1] += act
        if direction == "w":
            self.__hero[0] -= act
        if direction == "x":
            self.__hero[0] += act

    def __check_hero(self, direction, monster, field):
        field_height = len(field.getField())
        field_width = len(field.getField()[0])
        monster_flg = 0
        if self.__hero[0] < 0:
            self.__hero[0] = 0
        if self.__hero[1] < 0:
            self.__hero[1] = 0
        if self.__hero[0] > (field_height - 1):
            self.__hero[0] = field_height - 1
        if self.__hero[1] > (field_width - 1):
            self.__hero[1] = field_width - 1
        if self.__hero == monster:
            self.move(direction, -1)
            monster_flg += 1
        if "■" == field.getField()[self.__hero[0]][self.__hero[1]]:
            self.move(direction, -1)

        return monster_flg

    def action(self, monster, direction, field):
        self.move(direction, 1)
        return self.__check_hero(direction, monster, field)


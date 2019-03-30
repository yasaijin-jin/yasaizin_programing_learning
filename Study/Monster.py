#!/usr/bin python3
# -*- coding: utf-8 -*-

import random


class Monster(object):
    """
    Monster Class
    """
    __name = None
    __max_hp = None
    __hp = None
    __ap = None
    __dp = None

    __num = None

    __monster = None
    character = None

    def __init__(self, character, conf, h, w):
        """
        出現モンスターの初期値を設定
        """
        self.character = character
        self.__num = str(random.randint(1, 2))
        self.__name = conf.getParams("name", self.__num)
        self.__max_hp = conf.getParams("hp", self.__num)
        self.__hp = int(self.__max_hp)
        self.__ap = int(conf.getParams("ap", self.__num))

        self.__monster = [h, w]

    def giveAttack(self) -> int:
        """
        攻撃を与える
        :return:
        """
        return self.__ap

    def getName(self) -> str:
        """
        モンスターの名前を取得
        :return:
        """
        return self.__name

    def receiveDamage(self, damage) -> bool:
        """
        ダメージを受ける
        :param damage:
        :return:
        """
        return self.__check_damage(damage)

    def __check_damage(self, damage) -> bool:
        """
        ダメージをチェック
        :param damage:
        :return:
        """
        self.__hp -= damage
        if self.__hp <= 0:
            print("{}'s {} damage.".format(self.__name, damage))
            print("{}'s down.".format(self.__name))
            return True
        else:
            print("{}'s {} damage.".format(self.__name, damage))
            return False

    def getMonster(self):
        return self.__monster

    def action(self, monster_flg):
        if monster_flg == 1:
            if self.receiveDamage(self.character.getAttack()):
                self.__monster = None


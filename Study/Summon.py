#!/usr/bin python3
# -*- coding: utf-8 -*-

import Study.Character as Character
import Study.Monster as Monster
import Study.Field as Field

import Study.Config as Config

import readchar


if __name__ == "__main__":
    conf = Config.Config()
    field = Field.Field(conf)
    character = Character.Character(conf)
    monster = Monster.Monster(character, conf, 1, 4)

    print("{}が現れた".format(monster.getName()))
    goal = None
    for y in range(len(field.getField())):
        if "□" in field.getField()[y]:
            print(field.getField()[y])
            for x in range(len(field.getField()[y])):
                if "□" == field.getField()[y][x]:
                    goal = [y, x]

    field.setHero(character.getHero())
    field.setMonster(monster.getMonster())
    while 1:
        for h in field.getField():
            for w in h:
                print(w, end='')
            print()

        field.clear()
        kb = input()
        #kb = readchar.readchar()
        monster_flg = character.action(monster.getMonster(), kb, field)
        monster.action(monster_flg)
        field.setHero(character.getHero())
        field.setMonster(monster.getMonster())

        if goal == character.getHero():
            break

    for h in field.getField():
        for w in h:
            print(w, end='')
        print()

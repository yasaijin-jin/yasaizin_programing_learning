#!/usr/bin python3
# -*- coding: utf-8 -*-


class RandMaze(object):
    __height = None
    __width = None

    __maze = []

    def __init__(self, height, width):
        self.__setHeight(height)
        self.__setWidth(width)

    def __setHeight(self, height):
        self.__height = height

    def __setWidth(self, width):
        self.__width = width

    def getHeight(self):
        return self.__height

    def getWidth(self):
        return self.__width

    def __create_maze_row(self):
        maze_r = []
        [maze_r.append(0) for w in range(self.__width)]
        return maze_r

    def createMaze(self):
        __maze = []
        [__maze.append(self.__create_maze_row()) for h in range(self.__height)]
        for maze_r in __maze:
            for w in maze_r:
                print(w, end='')
            print()



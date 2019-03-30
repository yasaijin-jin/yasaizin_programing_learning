
import configparser as config


class Config(object):
    __conf = None

    def __init__(self):
        self.__conf = config.ConfigParser()
        self.__conf.read("./config.ini", "utf-8")
        self.__conf.sections()

    def getMapData(self, num):
        return self.__conf.get("MAP_DATA", "stage{}".format(num))

    def getParams(self, param, num=None):
        if num:
            return self.__conf.get("Monster{}".format(num), param)
        else:
            return self.__conf.get("Player", param)


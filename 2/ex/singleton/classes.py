#!/usr/bin/python

class Singleton(object):
    class __inner(object):
        def __init__(self, *args):
            self.a = args[0]
            self.b = args[1]

    __instance = None    

    def __init__(self, *args):
        if Singleton.__instance is None:
            Singleton.__instance = Singleton.__inner(*args)
    def __getattr__(self, attr):
        return getattr(self.__instance, attr)
    def __setattr__(self, attr, val):
        return setattr(self.__instance, attr, val)
    def getInstance(self):
        return self.__instance

# game.py
# Author: Sébastien Combéfis
# Version: February 8, 2016

from abc import *
import socket

class InvalidMoveException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Game(metaclass=ABCMeta):
    def __init__(self, name, nbplayers):
        self.__name = name
        self.__nbplayers = nbplayers
        self.__currentplayer = None
    
    @property
    def name(self):
        return self.__name
    
    @property
    def nbplayers(self):
        return self.__nbplayers
    
    @property
    def currentplayer(self):
        return self.__currentplayer
    
    @abstractmethod
    def applymove(self, move):
        ...
    
    @abstractmethod
    def isfinished(self):
        ...
    
    def _waitplayers(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((socket.gethostname(), 5000))
        s.listen()
        self.__players = []
        while len(self.__players) < self.__nbplayers:
            self.__players.append(s.accept())
    
    def _gameloop(self):
        self.__currentplayer = 0
        while not self.isfinished():
            pass
    
    def run(self):
        self._waitplayers()
        self._gameloop()
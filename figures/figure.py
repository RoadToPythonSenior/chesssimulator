from abc import ABC, abstractmethod
from enum import Enum


class Color(Enum):
    white = 1
    black = 2


class Figure(ABC):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    @abstractmethod
    def check_border(self, x , y, border):
        pass

    @abstractmethod
    def check_other_figure(self, x, y):
        pass

    @abstractmethod
    def move(self, x, y):
        pass

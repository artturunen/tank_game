import os
import sys
import pygame as pg
import math
from collision import Collider

WALL_COLOR = (105,105,105)

class Wall(object):

    def __init__(self, point1, point2):

        self.point1 = point1
        self.point2 = point2

        self.width = 7

        self.wall_angle = math.atan2(self.point2[1]-self.point1[1], self.point2[0] - self.point1[0]) * 180 / math.pi
        self.lenght = math.sqrt((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)

        self.collider = Collider(2, self, 1)

    def draw(self, screen):

        pg.draw.line(screen, WALL_COLOR, self.point1, self.point2, self.width)



import os
import sys
import pygame as pg
import math
from collision import Collider

class Bullet(object):



    def __init__(self, pos, angle, p):

        self.hits = 0

        self.p = p
        self.true_pos = pos
        self.angle = angle
        self.speed = 140
        self.timeToLive = 300
        self.max_bounce = 3

        self.bullet_image = pg.image.load("bullet.png")
        self.rect = self.bullet_image.get_rect()

        self.collider = Collider(1, self, 2)

        self.velx = math.cos(math.radians(self.angle * -1 - 90))
        self.vely = math.sin(math.radians(self.angle * -1 - 90))



    def draw(self, screen):

        self.rect.center = self.true_pos
        screen.blit(self.bullet_image, self.rect)

    def hit(self):

        pass

    def update(self, dt):


        wall_angle = self.collider.is_collided_to_wall()

        if wall_angle != None and self.hits == self.max_bounce:
            self.timeToLive = 0

        if wall_angle != None and self.hits < self.max_bounce:

            self.hits += 1
            if wall_angle == 90:
                self.velx = self.velx * -1
            else:
                self.vely = self.vely * -1




        tank = self.collider.bullet_collided_tank()
        if tank != 0 and self.timeToLive > 0:

            self.timeToLive = 0
            self.hit()
            print(tank.p)

        self.timeToLive = self.timeToLive - 1



        self.true_pos[0] += self.velx * self.speed * dt
        self.true_pos[1] += self.vely * self.speed * dt


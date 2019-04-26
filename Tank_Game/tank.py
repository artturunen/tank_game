import os
import sys
import pygame as pg
import math
from bullet import Bullet
from collision import Collider

'''
DIR_KEYS = {pg.K_LEFT: 1,
            pg.K_RIGHT: -1,
            pg.K_UP: 1,
            pg.K_DOWN: 1,
            pg.K_f: 1
            }
'''

class Tank(object):

    def __init__(self, pos ,DIR_KEYS, keys, p):



        self.p = p

        self.DIR_KEYS = DIR_KEYS
        self.controls = keys

        self.x = 0
        self.y = 0

        self.lock_1 = True

        self.true_pos = pos
        self.angle = 0
        self.speed = 0
        self.max_speed = 100
        self.rot_speed = 120
        self.acceleration = 80

        if p == 1:
            self.tank_image = pg.image.load("tank_p11.png")
        if p == 2:
            self.tank_image = pg.image.load("tank_p2.png")

        self.rect = self.tank_image.get_rect()

        self.bullets = []

        self.collider = Collider(0, self, 15)

        self.myfont = pg.font.SysFont("arial black", 17)
        self.healt = 10


    def accelerate(self, dt):
        if self.speed < self.max_speed:
            self.speed = dt*self.acceleration + self.speed

    def reverse(self, dt):
        if self.speed > int(-self.max_speed/2):
            self.speed = dt * -self.acceleration + self.speed

    def slowdown(self, dt):
        if self.speed > 1:
            self.speed = dt * -self.acceleration + self.speed
        elif self.speed < -1:
            self.speed = dt * self.acceleration + self.speed


    def update(self, keys, dt):



        for key in self.DIR_KEYS:
            if keys[key]:
                if key == self.controls[0] or key == self.controls[1]:
                    self.angle += self.DIR_KEYS[key] * self.rot_speed * dt
                if key == self.controls[2]:
                    self.accelerate(dt)
                if key == self.controls[3]:
                    self.reverse(dt)
                if key == self.controls[4] and self.lock_1:

                    pg.mixer.music.load("farts.mp3")
                    pg.mixer.music.play(0)

                    angle = self.angle
                    pos = [self.x + 15*math.cos(math.radians(angle * -1 - 90)), self.y + 15*math.sin(math.radians(angle * -1 - 90))]

                    self.bullets.append(Bullet(pos, angle, self.p))
                    self.lock_1 = False


        if keys[self.controls[2]] == 0 and keys[self.controls[3]] == 0:
            self.slowdown(dt)
        if keys[self.controls[4]] == 0:
            self.lock_1 = True


        self.oldx = self.true_pos[0]
        self.oldy = self.true_pos[1]

        self.true_pos[0] += math.cos(math.radians(self.angle * -1 - 90)) * self.speed * dt * self.DIR_KEYS[key]
        self.true_pos[1] += math.sin(math.radians(self.angle * -1 - 90)) * self.speed * dt * self.DIR_KEYS[key]

        if self.collider.is_collided() or self.collider.tank_collided_to_wall():

            self.true_pos[0] = self.oldx
            self.true_pos[1] = self.oldy

        self.x = self.true_pos[0]
        self.y = self.true_pos[1]

    def draw(self, screen):



        self.rotated = pg.transform.rotate(self.tank_image, self.angle)
        self.rect = self.rotated.get_rect()
        self.rect.center = self.true_pos

        label = self.myfont.render(str(self.healt), 10, (255,255,255))
        screen.blit(label, (self.true_pos[0]-14, self.true_pos[1]-40) )

        screen.blit(self.rotated, self.rect)

import os
import sys
import pygame as pg
from tank import Tank
from bullet import Bullet
from wall import Wall



BACKGROUND_COLOR = (107, 164, 0)


class App(object):

    def __init__(self):

        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.done = False
        self.keys = pg.key.get_pressed()

        p1keys = {pg.K_LEFT: 1,
                pg.K_RIGHT: -1,
                pg.K_UP: 1,
                pg.K_DOWN: 1,
                pg.K_k: 1
                }

        p1controls = [pg.K_LEFT, pg.K_RIGHT, pg.K_UP, pg.K_DOWN, pg.K_k]

        p2keys = {pg.K_a: 1,
                  pg.K_d: -1,
                  pg.K_w: 1,
                  pg.K_s: 1,
                  pg.K_g: 1
                  }
        p2controls = [pg.K_a, pg.K_d, pg.K_w, pg.K_s, pg.K_g]


        self.tanks = []
        tank = Tank([100,100], p1keys, p1controls, 1)
        tank2 = Tank([900,700], p2keys, p2controls, 2)
        self.tanks.append(tank)
        self.tanks.append(tank2)

        self.walls = []
        self.make_walls()


    def make_walls(self):

        self.walls.append(Wall((0, 0), (0, 800)))
        self.walls.append(Wall((0, 0), (1000, 0)))
        self.walls.append(Wall((1000, 0), (1000, 800)))
        self.walls.append(Wall((0, 800), (1000, 800)))

        self.walls.append(Wall((200,200),(200,600)))
        self.walls.append(Wall((800, 200), (800, 600)))

        self.walls.append(Wall((300, 400), (700, 400)))

        self.walls.append(Wall((500, 0), (500, 200)))
        self.walls.append(Wall((500, 600), (500, 800)))



    def event_loop(self):

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            elif event.type in (pg.KEYDOWN, pg.KEYUP):
                self.keys = pg.key.get_pressed()


    def render(self):

        self.screen.fill(BACKGROUND_COLOR)

        for tank in self.tanks:
            tank.draw(self.screen)

            for bullet in tank.bullets:
                bullet.draw(self.screen)

        for wall in self.walls:
            wall.draw(self.screen)

        pg.display.update()

    def update(self, dt):


        for tank in self.tanks:
            tank.update(self.keys, dt)

            for bullet in tank.bullets:

                bullet.update(dt)

                if bullet.timeToLive < 0:
                    tank.bullets.remove(bullet)

    def main_loop(self):

        dt = 0
        self.clock.tick(self.fps)
        while not self.done:
            self.event_loop()
            self.update(dt)
            self.render()
            dt = self.clock.tick(self.fps) / 1000.0


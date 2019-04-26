import os
import sys
import pygame as pg

from app import App

CAPTION = "Tank Game"
SCREEN_SIZE = (1000, 800)

def main():

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    pg.display.set_caption(CAPTION)
    pg.display.set_mode(SCREEN_SIZE)
    App().main_loop()
    pg.quit()
    sys.exit()


main()
# content from kids can code: http://kidscancode.org/blog/

# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random

# game settings 
WIDTH = 360
HEIGHT = 480
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.yvel = 5
        self.xvel = 5
        print(self.rect.center)
    def update(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if self.rect.x < 0:
            self.xvel*=-1
        if self.rect.y < 0:
            self.yvel*=-1
        if self.rect.x > WIDTH - self.rect.width:
            self.xvel*=-1
        if self.rect.y > HEIGHT - self.rect.height:
            self.yvel*=-1
        


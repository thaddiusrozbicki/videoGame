# content from kids can code: http://kidscancode.org/blog/

# sources


#  design
'''
Innovation:
Similar to Atari Breakout but with moving platforms

'''

# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from math import *
import time
from time import *
vec = pg.math.Vector2

# # game settings 
WIDTH = 360
HEIGHT = 480
FPS = 30
mpos = (0,0)

# player settings
PLAYER_GRAV = 0.9
PLAYER_FRIC = 0.1
SCORE = 0

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def draw_text(text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_surface, text_rect)

def colorbyte():
    return random.randint(0,255)

# create all classees as sprites...

# player sprite
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((100, 25))
        self.r = 0
        self.g = 0
        self.b = 255
        self.image.fill((self.r,self.g,self.b))
        self.rect = self.image.get_rect()
        # self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT-45)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.health = 100
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_d]:
            self.acc.x = 5
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, all_plats, False)
        self.rect.x += -1
        if hits:
            self.vel.y = -25
    def draw(self):
        pass
    def inbounds(self):
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.x > WIDTH:
            self.pos.x = WIDTH
    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # friction
        self.acc.x += self.vel.x * -0.1
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # self.rect.x += self.xvel
        # self.rect.y += self.yvel
        self.inbounds()
        self.rect.midbottom = self.pos

# platforms
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# bullet sprite

    # def update(self):
    #     if self.owner == "player":
    #         self.rect.y -= self.speed
    #     else:
    #         self.rect.y += self.speed
    #     if (self.rect.y < 0):
    #         self.kill()
    #         print(pewpews)

# here's the mobs
class Ball(Sprite):
    def __init__(self, x, y, w, h, color):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.color=color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed=5

    # def update(self):
    #     if Ball.rect.x>=360:
    #         Ball.velocity[0] = -Ball.velocity[0]
    #     if Ball.rect.x<=0:
    #         Ball.velocity[0] = -Ball.velocity[0]
    #     if Ball.rect.y>480:
    #         Ball.velocity[1] = -Ball.velocity[1]
    #     if Ball.rect.y<0:
    #         Ball.velocity[1] = -Ball.velocity[1] 
            
class Mob(Sprite):
    def __init__(self, x, y, w, h, color, typeof, health):
        Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.color = color
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.typeof = typeof
        self.initialized = False
        
    def init(self):
        self.initialized = True

    def update(self):
        self.rect.x += self.speed
        if self.typeof == "boss":
            if self.rect.right > WIDTH or self.rect.x < 0:
                self.speed *= -1
                self.rect.y += 15
        else:
            if self.rect.right > WIDTH or self.rect.x < 0:
                self.speed *= -1
     
            pass
# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()

# instantiate classes
player = Player()
ground = Platform(0, HEIGHT-40, WIDTH, 40)
ball1 = Ball(50,50,25,25,RED)

# create groups
all_sprites = pg.sprite.Group()
all_plats = pg.sprite.Group()
mobs = pg.sprite.Group()
ball = pg.sprite.Group()

# instantiate lots of mobs in a for loop and add them to groups
for i in range(15):
    m = Mob(randint(0,WIDTH-100), randint(75,HEIGHT/2), 75, 25, (colorbyte(),colorbyte(),colorbyte()), "normal", 5)
    all_sprites.add(m)
    mobs.add(m)
    m.init()
    print(m)

# add things to groups...
all_sprites.add(player, ground, ball)
all_plats.add(ground)

# Game loop
start_ticks = pg.time.get_ticks()
running = True
while running:
    # keep the loop running using clock
    delta = clock.tick(FPS)
    seconds = floor((pg.time.get_ticks()-start_ticks)/1000)
    hits = pg.sprite.spritecollide(player, all_plats, False)
    if hits:
        # print("ive struck a plat")
        player.pos.y = hits[0].rect.top
        player.vel.y = 0

        # if mhit:
        #     print('hit mob ' + str(mhit[0]))
    
    # mobhits = pg.sprite.spritecollide(player, mobs, True)

    # if mobhits:
    #     # print("ive struck a mob")
    #     player.health -= 1
    #     if player.r < 255:
    #         player.r += 15 

    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False



        
    ############ Update ##############
    # update all sprites
    all_sprites.update()

    ############ Draw ################
    # draw the background screen
      
    screen.fill(BLACK)
    # screen.fill(BLACK)

    # draw text
    draw_text("FPS: " + str(delta), 22, RED, 64, HEIGHT / 24)
    draw_text("Timer: " + str(seconds), 22, RED, 64, HEIGHT / 10)
    draw_text("POINTS: " + str(SCORE), 22, WHITE, WIDTH / 2, HEIGHT / 24)
    
    # draw player color
    player.image.fill((player.r,player.g,player.b))
    
    # draw all sprites
    all_sprites.draw(screen)

    # buffer - after drawing everything, flip display
    pg.display.flip()

pg.quit()

# content from kids can code: http://kidscancode.org/blog/

# import libraries and modules
# from platform import platform
import pygame as pg
from pygame.sprite import Sprite
import random

vec = pg.math.Vector2

# game settings 
WIDTH = 360
HEIGHT = 480
FPS = 30
PLAYER_GRAV=.98
# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# all characters with Sprite as a superclass and Player as a subclass
class Player(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.image = pg.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.pos = vec(WIDTH/2, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        # tells player how to move
    def controls(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a]:
            self.acc.x = -5
            # print(self.vel)
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_w]:
            self.acc.y = -5
            # print(self.vel)
        if keys[pg.K_s]:
            self.acc.y = 5
            # gives movement
    

    def update(self):
        self.acc = vec(0,PLAYER_GRAV)
        self.controls()
        # self.vel.y=20
        # friction
        self.acc.x += self.vel.x * -0.1
        self.acc.y += self.vel.y * -0.1
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # self.rect.x += self.xvel
        # self.rect.y += self.yvel
        self.rect.midbottom = self.pos
# inanimate platform
class Platform(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        

# init pygame and create a window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("My Game...")
clock = pg.time.Clock()
  
# create a group for all sprites
all_sprites = pg.sprite.Group()
all_plats = pg.sprite.Group()
# instantiate the player class
player = Player()
plat = Platform(WIDTH/2, HEIGHT/3, 100, 35)
plat1 = Platform(0, 400, 400, 10)

# add player to all sprites group
all_sprites.add(player)
all_sprites.add(plat)
all_sprites.add(plat1)

all_sprites.add(player)
all_plats.add(plat, plat1)

all_sprites.add(plat)
all_sprites.add(plat1)
class Enemy(Sprite):
    def __init__(self,name,shield,destruction):
        self.name=name
        self.shield=shield
        self.destruction=destruction
    def greeting(self):
        print('Hello, I am ' +self.name)
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Game loop
# keeps game runnint until QUIT
# says that at all times, while the game is running, run the if statment to check if player is interacting with 
# platform and if so to print something and to freeze the y coordinates of the player
running = True
while running:
    # keep the loop running using clock
    clock.tick(FPS)
    hits = pg.sprite.spritecollide(player, all_plats, False)
    if hits:
        print("ive struck a plat")
        player.pos.y = hits[0].rect.top
        player.vel.y = 0
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
    # draw all sprites
    all_sprites.draw(screen)

    # buffer - after drawing everything, flip display
    pg.display.flip()

pg.quit()

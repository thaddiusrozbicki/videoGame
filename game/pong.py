import pygame
from random import randint
BLACK = (0,0,0)


class Ball(pygame.sprite.Sprite):
    #This class represents a ball. It derives from the "Sprite" class in Pygame.
    
    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
 
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        self.velocity = [randint(4,8),randint(-8,8)]
        
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]


pygame.init()

# Define some colors
BLACK = (0,0,0)
WHITE = (255,255,255)

# Open a new window


# paddleA = Paddle(WHITE, 10, 100)
# paddleA.rect.x = 20
# paddleA.rect.y = 200

# paddleB = Paddle(WHITE, 10, 100)
# paddleB.rect.x = 670
# paddleB.rect.y = 200

ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

#This will be a list that will contain all the sprites we intend to use in our game.
all_sprites_list = pygame.sprite.Group()

# Add the paddles and the ball to the list of objects
# all_sprites_list.add(paddleA)
# all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

# The loop will carry on until the user exits the game (e.g. clicks the close button).

 
# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------

 
    #Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B) 
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     paddleA.moveUp(5)
    # if keys[pygame.K_s]:
    #     paddleA.moveDown(5)
    # if keys[pygame.K_UP]:
    #     paddleB.moveUp(5)
    # if keys[pygame.K_DOWN]:
    #     paddleB.moveDown(5)    
 
    # --- Game logic should go here
    # all_sprites_list.update()
 
    #Check if the ball is bouncing against any of the 4 walls:



 

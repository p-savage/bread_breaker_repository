import pygame
from random import choice

class Ball:
    """Class to handle the ball"""

    def __init__(self, bb_game):
        """Initialize the ball and set its starting position"""
        #link to the screen and settings
        self.screen = bb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = bb_game.settings
       
        #get the image
        self.image_raw = pygame.image.load('images/ball_bread.png')
        self.image = pygame.transform.smoothscale(self.image_raw, (40,40))
        #get the rectangle
        self.rect = self.image.get_rect()
        self.rect.inflate_ip(-2,-2)
        self.radius = self.rect.width //2
       
        #set its starting position
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 125
        #store exact x and y position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
       
        #set movement tracker
        self.moving = False
        #set the vector
        self.vector = pygame.math.Vector2()

    def update(self):
        """Move the ball"""
        if self.moving == True:
            self.x += self.vector.x
            self.y += self.vector.y
            self.rect.x, self.rect.y = self.x, self.y

    def rand_up_dir(self):
        """Generates a random upward direction"""
        x_choices = [-1,0,1]
        self.vector.x = choice(x_choices) * self.settings.ball_speed
        self.vector.y = self.settings.ball_speed * -1

    def reset_pos(self):
        """Reset the ball at its starting position"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom - 125
        self.x = self.rect.x
        self.y = self.rect.y

    def draw(self):
        """Draw the ball to the screen"""
        self.screen.blit(self.image, (self.rect.x, self.rect.y-2))
        ##red rect and green circle for hitbox debugging, delete when done
        pygame.draw.rect(self.screen, (255,0,0), self.rect, 2)
        pygame.draw.circle(
            self.screen,
            (0,255,0),
            self.rect.center,
            self.radius,
            1
        )
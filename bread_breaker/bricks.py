import pygame
from pygame.sprite import Sprite

class Bricks(Sprite):
    """Class to handle the brick bread"""

    def __init__(self, bb_game):
        """Initialize the bricks"""
        super().__init__()
        self.screen = bb_game.screen
        self.screen_rect = self.screen.get_rect()
        self.image_raw = pygame.image.load('images/brick_bread1.png')
        self.image_rotated = pygame.transform.rotate(self.image_raw, 90)
        self.image = pygame.transform.smoothscale(self.image_rotated,
                                                  (120,40))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = self.rect.height

    def draw_hitbox(self):
        """Draws a rect for hitbox refinement"""     
        #red rect for hitbox refinement; delete when done
        pygame.draw.rect(
            self.screen,
            (255,0,0),
            self.rect,
            1
        )
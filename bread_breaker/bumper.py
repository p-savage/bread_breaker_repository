import pygame

class Bumper:
    """A class to manage the bumper"""

    def __init__(self, bb_game):
        """Initialize the bumper and set its starting position"""
        #link to the game window and its rect
        self.screen = bb_game.screen
        self.screen_rect = self.screen.get_rect()
        #link to settings
        self.settings = bb_game.settings
        #draw the bumper image
        self.image_raw = pygame.image.load(
            'images/bumper_bread.png').convert_alpha()
        self.image_rotated = pygame.transform.rotate(self.image_raw, 90)
        self.image = pygame.transform.smoothscale(self.image_rotated,
                                                  (240,60))
        #get its rect
        self.rect = self.image.get_rect()
        #set it at the bottom middle of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = (self.screen_rect.bottom - 15)
        #store the exact x position
        self.x = float(self.rect.x)
        #movement flags
        self.moving_left = False
        self.moving_right = False

    def update(self):
        """Updates bumper x position"""
        if (self.moving_left
            and self.rect.left > 0):
            self.x -= self.settings.bumper_speed
        if (self.moving_right
            and self.rect.right < self.screen_rect.right):
            self.x += self.settings.bumper_speed
        self.rect.x = self.x

    def show_bumper(self):
        """Draw the bumper on the screen"""
        self.screen.blit(self.image, self.rect) 
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
        self.image = pygame.Surface((120, 20))
        self.image.fill("blue")
        #get its rect
        self.image_rect = self.image.get_rect()
        #set it at the bottom middle of the screen
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.bottom = (self.screen_rect.bottom - 15)

    def show_bumper(self):
        """Draw the bumper on the screen"""
        self.screen.blit(self.image, self.image_rect)
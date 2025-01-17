import pygame

class Settings:
    """A class to handle game settings"""

    def __init__(self):
        """Initialize game settings"""
        #screen dimensions and color
        self.screen_width = 1600
        self.screen_height = 800
        self.bg_image_raw = pygame.image.load('images/floured_background.bmp')
        self.bg_image = pygame.transform.smoothscale(self.bg_image_raw,
            (1600,800)) 
        #bumper speed
        self.bumper_speed = 20
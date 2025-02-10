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
        #set the edge objects for use in collision detection
        self.top_edge = pygame.Rect(0,0,self.screen_width,-1)
        self.bottom_edge = pygame.Rect(0,803,self.screen_width,1)
        self.right_edge = pygame.Rect(1600,0,1,self.screen_height)
        self.left_edge = pygame.Rect(-1,0,1,self.screen_height)
        #bumper speed
        self.bumper_speed = 12
        #ball speed
        self.ball_speed = 3

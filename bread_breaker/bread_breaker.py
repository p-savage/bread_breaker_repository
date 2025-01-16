import pygame
import sys

from settings import Settings
from bumper import Bumper

class BreadBreaker:
    """A class to initiate the game"""
    
    def __init__(self):
        """Initialize game elements"""
        #create game window
        pygame.init()
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height))
        self.screen.fill(self.settings.bg_color)
        pygame.display.set_caption('Bread-Breaker')

        self.bumper = Bumper(self)
        
        self.clock = pygame.time.Clock()

    def run_game(self):
        """Handle the main game loop"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
            self.bumper.show_bumper()
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    bb = BreadBreaker()
    bb.run_game()
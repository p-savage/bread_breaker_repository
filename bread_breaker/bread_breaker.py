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
        self.screen.blit(self.settings.bg_image, (0,0))
        pygame.display.set_caption('Bread Breaker')

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
                    elif event.key == pygame.K_RIGHT:
                        self.bumper.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.bumper.moving_left = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.bumper.moving_right = False
                    elif event.key == pygame.K_LEFT:
                        self.bumper.moving_left = False
            self.bumper.update()
            self._update_screen()
            self.clock.tick(60) 

    def _update_screen(self):
        """Draws a new frame and shows it"""
        self.screen.blit(self.settings.bg_image, (0,0))
        self.bumper.show_bumper()
        pygame.display.flip()
            

if __name__ == '__main__':
    bb = BreadBreaker()
    bb.run_game()
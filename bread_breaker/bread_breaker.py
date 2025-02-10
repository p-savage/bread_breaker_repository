import pygame
import sys

from settings import Settings
from bumper import Bumper
from bricks import Bricks
from ball import Ball

class BreadBreaker:
    """A class to initiate the game"""
    
    def __init__(self):
        """Initialize game elements"""
        #create game window
        pygame.init()
        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
            self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        self.screen.blit(self.settings.bg_image, (0,0))
        pygame.display.set_caption('Bread Breaker')

        self.bumper = Bumper(self)
        self.bricks = pygame.sprite.Group()
        self.ball = Ball(self)

        self._create_array()

        self.clock = pygame.time.Clock()

    def run_game(self):
        """Handle the main game loop"""
        while True:
            self._check_key_events()
            self._check_collisions()
            self.bumper.update()
            self.ball.update()
            self._update_screen()
            self.clock.tick(60) 

    def _check_key_events(self):
        """Handle key events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)   
            elif event.type == pygame.KEYUP:
                self._keyup_events(event)

    def _keydown_events(self, event):
        """Handle key presses"""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_RIGHT:
            self.bumper.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.bumper.moving_left = True
        elif (event.key == pygame.K_SPACE
              and self.ball.moving == False):
            self.ball.rand_up_dir()
            self.ball.moving = True
           

    def _keyup_events(self, event):
        """Handle key releases"""
        if event.key == pygame.K_RIGHT:
            self.bumper.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.bumper.moving_left = False

    def _check_collisions(self):
        """Look for collisions and send appropriate response call"""
        for brick in self.bricks:
            if self.ball.rect.colliderect(brick):
                self.bricks.remove(brick)
                self.ball.vector.y = self.ball.vector.y * -1
        if self.ball.rect.colliderect(self.bumper):
            self.ball.vector.y = self.ball.vector.y * -1
        if self.ball.rect.colliderect(self.settings.right_edge):
            self.ball.vector.x = self.ball.vector.x * -1
        if self.ball.rect.colliderect(self.settings.left_edge):
            self.ball.vector.x = self.ball.vector.x * -1
        if self.ball.rect.colliderect(self.settings.top_edge):
            self.ball.vector.y = self.ball.vector.y * -1
        if self.ball.rect.colliderect(self.settings.bottom_edge):
            self.ball.moving =  False
            self.ball.reset_pos()

            

    def _create_array(self):
        """Create the brick pattern"""
        brick = Bricks(self)
        brick_width = brick.rect.width
        current_x = 0
        current_y = brick.rect.height
        while current_y < 480:
            while (self.settings.screen_width - current_x) > brick_width: 
                new_brick = Bricks(self)
                new_brick.rect.x = current_x
                new_brick.rect.y = current_y
                self.bricks.add(new_brick)
                current_x += brick_width
            current_x = 0
            current_y += new_brick.rect.height

    def _update_screen(self):
        """Draws a new frame and shows it"""
        self.screen.blit(self.settings.bg_image, (0,0))
        self.bricks.draw(self.screen)
        self.bumper.show_bumper()
        self.ball.draw()
        pygame.display.flip()
            

if __name__ == '__main__':
    bb = BreadBreaker()
    bb.run_game()
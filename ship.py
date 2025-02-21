
import pygame
from  pygame.sprite import Sprite

class Ship(Sprite):
    """class of manage ship"""

    def __init__(self,ai_game):
        """init the settings and position of the ship"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # put the new ship at the bottom of the screen
        self.image = pygame.image.load('images/ship.jpeg')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # store the minimum value in the attribute of the ship
        self.x = float(self.rect.x)

        # moving tag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """adjust the position of the ship according to the moving tag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left >0:
            self.x -= self.settings.ship_speed
        # truncated display x
        self.rect.x = self.x

    def blitme(self):
        """draw ship"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
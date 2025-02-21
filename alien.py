
import pygame

from pygame.sprite import Sprite

class Alien(Sprite):
    """class of manage alien"""

    def __init__(self,ai_game):
        """init the settings and position of the alien"""
        super().__init__()
        self.screen = ai_game.screen

        # load picture and set position
        self.image = pygame.image.load('images/alien.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y =self.rect.height
        self.settings = ai_game.settings

        # store the x value of the alien
        self.x = float(self.rect.x)

        # # moving tag
        # self.moving_right = False
        # self.moving_left = False
        # self.settings = ai_game.settings
        # self.screen_rect = ai_game.screen.get_rect()

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """adjust the position"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

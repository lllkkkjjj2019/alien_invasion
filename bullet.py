import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """class of manage bullet"""

    def __init__(self,ai_game):
        """create a Bullet object at th current position of the ship"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        """create th rectangle of bullet"""
        self.rect = pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        """store the position of the bullet by float"""
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet up"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draw the bullet on the screen"""
        pygame.draw.rect(self.screen,self.color,self.rect)
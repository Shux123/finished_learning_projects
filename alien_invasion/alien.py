from typing import Any
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    #Class for an alien in the game
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        

        #Load the alien's image and get it rect
        self.image = pygame.image.load(
            'D:\Python\projects\\alien_invasion\images\\alien.bmp')
        self.rect = self.image.get_rect()
        
        #Start new alien near the top left side of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact horisontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        #Returns true if alien is at edge of the screen
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        #Move the alien to the right or left
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
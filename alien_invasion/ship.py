import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    #Class to manage a ship.

    def __init__(self, ai_game):
        #Initializate the ship and set it starting position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and get it rectangle
        self.image = pygame.image.load(
            'D:\Python\projects\\alien_invasion\images\ship.bmp'
        )
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        #Store a float for the ship's exact horisontal position
        self.x = float(self.rect.x)

        #Movement flag starts with ship that has no moving
        self.moving_right = False
        self.moving_left = False
    
    def blitme(self):
        #Draw the ship at its current location.
        self.screen.blit(self.image, self.rect)

    def update(self):
        #Update ship position based on the moving flag.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        #Update rectangle object from self.x
        self.rect.x = self.x

    def center_ship(self):
        #Center the ship on the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
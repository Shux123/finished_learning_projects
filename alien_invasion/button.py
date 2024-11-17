import pygame.font

class   Button:
    '''Represents a button in a game'''
    def __init__(self, ai_game, msg):
        #Initialize the button for the game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #Set dimmentions and properties for the button
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #Build the button object and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #The button message needs to be prepared only once
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        #Turn msg into rendered image and center text on the button
        self.msg_image = self.font.render(msg, True, self.text_color, 
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''Draw blank button and then draw message'''
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
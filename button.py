import pygame.font

class Button:
    """A class to build buttons for the game."""
    
    def __init__(self, ai_game, msg):
        """Initiliaze button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        # The button message need to be prepped only once.
        self._prep_msg(msg)
    
    def _prep_msg(self, msg):
        """Turn sg into a rendered image and center text on the button."""
        self._msg_image = self.font.render(msg, True, self.text_color,
                                           self.button_color)
        self.msg_image_rect = self._msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self._msg_image, self.msg_image_rect)
import pygame

class Button():
  """Button class"""
  def __init__(self, screen, settings, message):
    self.screen     = screen
    self.width      = settings.button_width
    self.height     = settings.button_height
    self.color      = settings.button_color
    self.text_color = settings.text_color
    self.text       = message
    self.font       = pygame.font.SysFont(None, 48)

    self.rect        = pygame.Rect(0, 0, self.width, self.height)
    self.rect.center = self.screen.get_rect().center

  def prepare_message(self):
    """Message for button"""
    self.msg_image = self.font.render(self.text, True, self.text_color,
    self.color)
    self.msg_rect  = self.msg_image.get_rect()
    self.msg_rect.center = self.rect.center

  def draw_button(self):
    """Draw button """
    self.screen.fill(self.color, self.rect)
    self.prepare_message()
    self.screen.blit(self.msg_image, self.msg_rect)

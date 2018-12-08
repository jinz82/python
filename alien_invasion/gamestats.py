import pygame
from pygame.sprite import Sprite, Group
from ship import Ship

class GameStats(Sprite):
  """Stats for gameplay"""
  def __init__(self, settings, screen):
    super(GameStats, self).__init__()
    self.screen        = screen
    self.color         = (30,30,30)
    self.high_score    = 0
    self.current_score = 0
    self.ships         = Group()
    self.ships_left    = settings.ships_left
    self.alien_points  = settings.alien_points
    self.speed_current = settings.speed_factor
    self.font          = pygame.font.SysFont(None, settings.score_font)
    self.offsety       = settings.score_y
    self.background    = settings.bg_color

  def prepare_score(self):
    """Prepare score to show"""
    if (self.high_score < self.current_score):
      self.high_score = self.current_score
    self.himage = self.font.render("High Score:"+str(self.high_score), True, self.color, self.background)
    self.cimage = self.font.render("Score:"+str(self.current_score), True, self.color, self.background)
    self.simage = self.font.render("Ships Left:"+str(self.ships_left), True, self.color, self.background)

    self.himage_rect = self.himage.get_rect()
    self.cimage_rect = self.cimage.get_rect()
    self.simage_rect = self.simage.get_rect()    

    self.himage_rect.center = self.screen.get_rect().center
    self.himage_rect.y      = self.offsety

    self.cimage_rect.right  = self.screen.get_rect().right - int(self.offsety)
    self.cimage_rect.y      = self.offsety

    self.simage_rect.left  = self.screen.get_rect().left + int(self.offsety)
    self.simage_rect.y      = self.offsety
   
  def show_stats(self):
    """ Display all stats on screen"""
    self.prepare_score()
    self.screen.blit(self.himage, self.himage_rect)
    self.screen.blit(self.cimage, self.cimage_rect)
    self.screen.blit(self.simage, self.simage_rect)
    



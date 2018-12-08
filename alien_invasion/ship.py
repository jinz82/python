import pygame
from pygame.sprite import Sprite, Group

class Ship(Sprite):
 """ Ship class"""
 def __init__(self, screen):
  super(Ship,self).__init__()
  self.speed      = 2
  self.move_left  = 0
  self.move_right = 0
  self.screen = screen
  self.image  = pygame.image.load('images/raptor_small.bmp')
  self.rect   = self.image.get_rect()

  self.rect.centerx = screen.get_rect().centerx
  self.rect.bottom  = screen.get_rect().bottom

 def draw_ship(self):
  """Draws ship on screen"""
  if self.move_left == True:
   if self.rect.left > self.screen.get_rect().left:
    self.rect.centerx-= self.speed
  if self.move_right == True:
   if self.rect.right < self.screen.get_rect().right:
    self.rect.centerx+= self.speed
  self.screen.blit(self.image, self.rect)


def recenter_ship(ship):
  """Recenters ship after one down"""
  ship.rect.centerx = ship.screen.get_rect().centerx
  ship.rect.bottom  = ship.screen.get_rect().bottom

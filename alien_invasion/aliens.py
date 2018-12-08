import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group

class Alien(Sprite):
 """Aliens of the game"""
 def __init__(self, screen):
  super(Alien, self).__init__()
  self.speed      = 1
  self.direction  = 1
  self.rows       = 4
  self.screen     = screen
  self.image      = pygame.image.load('images/alien_small.bmp')
  self.rect       = self.image.get_rect()

  self.rect.x     = self.rect.width
  self.rect.y     = self.rect.height

 def draw_alien(self):
  self.screen.blit(self.image, self.rect)

def create_fleet(screen, alien_number, alien_instance, alien_group):
 for row in range(alien_instance.rows):
  for alien in range(alien_number):
   new_alien = Alien(screen)
   new_alien.rect.x = (alien_instance.rect.width + 2*alien*alien_instance.rect.width)
   new_alien.rect.y = (alien_instance.rect.height) + (row*alien_instance.rect.height)
   alien_group.add(new_alien)

def draw_fleet(group,ai_set,ship):

  if (ai_set.game_active == 1):
    for every_alien in group.sprites():
      if (alien_at_edge(every_alien) == 1):
          ai_set.direction *= -1
          for every_alien in group.sprites():
            every_alien.rect.y +=every_alien.rect.height
            if (every_alien.rect.bottom >= ship.rect.top):
              print("Ship hit 1")
          break

    if pygame.sprite.spritecollideany(ship, group):
      print("Ship hit")

  for every_alien in group.sprites():
    if (ai_set.game_active == 1):
      every_alien.rect.x += every_alien.speed * ai_set.direction
    every_alien.draw_alien()

def alien_at_edge(alien):
  if ((alien.rect.right >= alien.screen.get_rect().right) or (alien.rect.left <= alien.screen.get_rect().left)):
   return 1
  else:
   return 0 

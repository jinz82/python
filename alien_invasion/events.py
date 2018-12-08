import sys
import pygame
from ship import Ship
from bullets import Bullet

def check_events(ship, screen, settings, group, button):
  """ Handles all events in game """
  if (settings.game_active == 1):
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
      sys.exit()
     elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
       ship.move_right = True
      if event.key == pygame.K_LEFT:
       ship.move_left = True
      if event.key == pygame.K_SPACE:
       if len(group) < settings.bullets_max:
        new_bullet = Bullet(ship,screen,settings)
        group.add(new_bullet)
     elif event.type == pygame.KEYUP:
      if event.key == pygame.K_RIGHT:
       ship.move_right = False
      if event.key == pygame.K_LEFT:
       ship.move_left = False
  else:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
       sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if button.rect.collidepoint(mouse_x, mouse_y):
          settings.game_active = 1
     

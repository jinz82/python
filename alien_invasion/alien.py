import sys
import pygame
from settings import Settings
from ship import Ship, recenter_ship
from aliens import Alien, create_fleet, draw_fleet
from events import check_events
from pygame.sprite import Group
from button import Button
from bullets import Bullet, draw_bullets
from gamestats import GameStats

def run_game():
 pygame.init()
 ai_set     = Settings()
 bullet_grp = Group()
 aliens_grp = Group()

 screen = pygame.display.set_mode((ai_set.screen_width ,ai_set.screen_height))
 pygame.display.set_caption("Space Invadors")
 screen.fill(ai_set.bg_color)
 button     = Button(screen, ai_set, "Play")
 stats      = GameStats(ai_set, screen)
 
 ai_ship  = Ship(screen)
 ai_alien = Alien(screen)

 # Mathematics of number of aliens and formation.
 x_space         = (ai_set.screen_width - 2*(ai_alien.rect.width))
 aliens_per_line = x_space/(2*(ai_alien.rect.width))
 create_fleet(screen, aliens_per_line, ai_alien, aliens_grp)

 while True:
  check_events(ai_ship, screen, ai_set, bullet_grp, button)
  screen.fill(ai_set.bg_color)
  ai_ship.draw_ship()
  draw_bullets(bullet_grp, aliens_grp, ai_set, stats)
  if (ai_set.game_active == 1):
    if (len(aliens_grp) == 0):
      bullet_grp.empty()
      create_fleet(screen, aliens_per_line, ai_alien, aliens_grp)
      recenter_ship(ai_ship)
    for every_b in bullet_grp.sprites():
      every_b.update_bullet()
  else:
    button.draw_button()
  draw_fleet(aliens_grp,ai_set, ai_ship)
  stats.show_stats()
  pygame.display.flip()

run_game()

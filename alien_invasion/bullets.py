import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
 """Instance of a bullet """
 def __init__(self, ship, screen, settings):
  super(Bullet, self).__init__()
  self.screen = screen
  self.rect   = pygame.Rect(0, 0, settings.bullet_width, settings.bullet_height)
  self.rect.centerx = ship.rect.centerx
  self.rect.top     = ship.rect.top
  self.color        = settings.bullet_color
  self.speed        = settings.bullet_speed
 def update_bullet(self):
  """Move the bullet up the screen."""
  self.rect.y = self.rect.y - self.speed

 def draw_bullet(self):
  """Draw the bullet to the screen."""
  pygame.draw.rect(self.screen, self.color, self.rect)

def draw_bullets(group, group_aliens, settings, stats):
  """Draws fired bullets """
  if (settings.game_active == 1):
    for every_bullet in group.sprites():
      every_bullet.draw_bullet()
      if every_bullet.rect.bottom < every_bullet.screen.get_rect().top:
        group.remove(every_bullet)
    collision = pygame.sprite.groupcollide(group, group_aliens, True, True)
    for collide in collision.values():
      stats.current_score += (stats.alien_points)

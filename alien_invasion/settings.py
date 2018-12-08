
class Settings():
 """A class to store all settings for Alien Invasion."""
 def __init__(self):
  """Initialize the game's settings."""
  # Screen settings
  self.screen_width = 800
  self.screen_height = 640
  self.bg_color = (255, 255, 255)

  # Ship settings
  self.ships_left = 3
  
  # Bullet settings.
  self.bullets_max   = 5
  self.bullet_speed  = 4
  self.bullet_height = 8
  self.bullet_width  = 3
  self.bullet_color   = 60,60,60

  # Aliens Direction
  self.direction    = 1
  self.alien_points = 10
  
  # Game off by default.
  self.game_active  = 0
  self.speed_factor = 1

  # Button settings.
  self.button_width, self.button_height = 200, 50  
  self.button_color = (200,200,200)
  self.text_color   = (80, 80, 80)

  # Scoreboard settings
  self.score_y      = 5
  self.score_font   = 30



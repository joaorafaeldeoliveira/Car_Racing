from code.Const import C_CYAN, C_WHITE, EVENT_ENEMY, MENU_OPTION, SPAWN_TIME, WIN_HEIGHT, C_GREEN, EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL, WIN_WIDTH, C_RED, EVENT_SCORE, SCORE_TIME
from code.Entity import Entity
from code.Player import Player
from code.Enemy import Enemy
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from pygame.font import Font
import pygame
import random


class Level:

  def __init__(self, window, name: str, game_mode: str):

    self.timeout = TIMEOUT_LEVEL
    self.window = window
    self.name = name
    self.game_mode = game_mode
    self.entity_list: list[Entity] = []
    self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
    player = EntityFactory.get_entity('Player1')
    self.entity_list.append(player)

    if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
      player = EntityFactory.get_entity('Player2')
      self.entity_list.append(player)

    pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
    pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)
    pygame.time.set_timer(EVENT_SCORE, SCORE_TIME)

  def run(self):
    clock = pygame.time.Clock()
    while True:
      clock.tick(60)
      for ent in self.entity_list:
        self.window.blit(source=ent.surf, dest=ent.rect)
        ent.move()
        
        # Update damage cooldown
        if hasattr(ent, 'damage_cooldown') and ent.damage_cooldown > 0:
          ent.damage_cooldown -= 1
        
        if isinstance(ent, (Player, Enemy)):
          if ent.name == 'Player1':
            health_color = C_GREEN if ent.health > 3 else C_RED
            self.level_text(14, f'Player1: {ent.health} | Score: {ent.score}',
                            health_color, (10, 25))
          if ent.name == 'Player2':
            health_color = C_CYAN if ent.health > 3 else C_RED
            self.level_text(14, f'Player2: {ent.health} | Score: {ent.score}',
                            health_color, (10, 45))
      
      # Check collisions and apply damage
      EntityMediator.verify_collision(self.entity_list)
      
      # Remove dead entities (health <= 0)  
      EntityMediator.verify_health(self.entity_list)
      
      # Remove enemies that went off-screen
      self.entity_list = [
          ent for ent in self.entity_list
          if not (isinstance(ent, Enemy) and ent.rect.top > WIN_HEIGHT)
      ]
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit()

        if event.type == EVENT_ENEMY:
          choice = random.choice(('Enemy1', 'Enemy2'))
          self.entity_list.append(EntityFactory.get_entity(choice))
        
        if event.type == EVENT_SCORE:
          # Increase score every second for all players
          for ent in self.entity_list:
            if isinstance(ent, Player):
              ent.score += 10  # Add 10 points every second
        
        if event.type == EVENT_TIMEOUT:
          self.timeout -= TIMEOUT_STEP
          if self.timeout == 0:
            for ent in self.entity_list:
              if isinstance(ent, Player) and ent.name == 'Player1':
                pass
              if isinstance(ent, Player) and ent.name == 'Player2':
                pass
            return True

      found_player = False
      for ent in self.entity_list:
        if isinstance(ent, Player):
          found_player = True

      if not found_player:
        return False

      pygame.display.flip()

  def level_text(self, text_size: int, text: str, text_color: tuple,
                 text_pos: tuple):
    text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter",
                                          size=text_size)
    text_surf: pygame.Surface = text_font.render(text, True,
                                                 text_color).convert_alpha()
    text_rect: pygame.Rect = text_surf.get_rect(left=text_pos[0],
                                                top=text_pos[1])
    self.window.blit(source=text_surf, dest=text_rect)

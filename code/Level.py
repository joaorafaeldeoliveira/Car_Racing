from code.Const import C_CYAN, C_WHITE, EVENT_ENEMY, MENU_OPTION, SPAWN_TIME, WIN_HEIGHT, C_GREEN, EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL
from code.Entity import Entity
from code.Player import Player
from code.Enemy import Enemy
from code.EntityFactory import EntityFactory
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

    pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
    pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

  def run(self):
    clock = pygame.time.Clock()
    while True:
      clock.tick(60)
      for ent in self.entity_list:
        self.window.blit(source=ent.surf, dest=ent.rect)
        ent.move()

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

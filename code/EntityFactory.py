from code.Background import Background
from code.Player import Player
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Enemy import Enemy
import random


class EntityFactory:

  @staticmethod
  def get_entity(entity_name: str, position=(0, 0)):
    match entity_name:
      case 'Level1Bg':
        list_bg = []
        for i in range(3):
          list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
          list_bg.append(Background(f'Level1Bg{i}', (0, WIN_HEIGHT)))
        return list_bg

      case 'Level2Bg':
        list_bg = []
        for i in range(3):
          list_bg.append(Background(f'Level2Bg{i}', (0, 0)))
          list_bg.append(Background(f'Level2Bg{i}', (0, WIN_HEIGHT)))
        return list_bg

      case 'Player1':
        return Player('Player1', (WIN_WIDTH / 2 - 50, WIN_HEIGHT - 100))

      case 'Player2':
        return Player('Player2', (WIN_WIDTH / 2 + 50, WIN_HEIGHT - 100))

      case 'Enemy1':
        return Enemy('Enemy1', (random.randint(95, 400), -WIN_HEIGHT))

      case 'Enemy2':
        return Enemy('Enemy2', (random.randint(95, 400), -WIN_HEIGHT))

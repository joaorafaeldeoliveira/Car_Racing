from code.Background import Background
from code.Player import Player
from code.Const import WIN_HEIGHT, WIN_WIDTH


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

      case 'Player1':
        return Player('Player1', (10, WIN_HEIGHT))

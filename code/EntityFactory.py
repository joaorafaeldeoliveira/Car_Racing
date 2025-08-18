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
          # Position backgrounds to create seamless scrolling
          y_position = -WIN_HEIGHT * i  # Stack them vertically off-screen
          list_bg.append(Background(f'Level1Bg{i}', (0, y_position)))
        return list_bg

      case 'Player1':
        return Player('Player1', (10, WIN_HEIGHT))

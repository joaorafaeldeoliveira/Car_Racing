from code.Entity import Entity
from code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH


class Background(Entity):

  def __init__(self, name: str, position: tuple):
    super().__init__(name, position)

  def move(self):
    self.rect.centery -= ENTITY_SPEED[self.name]
    if self.rect.top <= 0:
      self.rect.bottom = WIN_HEIGHT

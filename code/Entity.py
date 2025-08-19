from abc import ABC, abstractmethod
import pygame.image
from code.Const import ENTITY_DAMAGE,ENTITY_HEALTH,ENTITY_SCORE


class Entity(ABC):

  def __init__(self, name: str, position: tuple):
    self.name = name
    self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
    self.rect = self.surf.get_rect(left=position[0], top=position[1])
    self.speed = 0
    self.health = ENTITY_HEALTH[self.name]
    self.damage = ENTITY_DAMAGE[self.name]
    self.last_dmg = 'None'
    self.score = ENTITY_SCORE[self.name]
    self.damage_cooldown = 0

  @abstractmethod
  def move(self, ):
    pass

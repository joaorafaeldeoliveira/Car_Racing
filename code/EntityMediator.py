from code.Player import Player
from code.Background import Background
from code.Const import WIN_WIDTH
from code.Entity import Entity
from code.Enemy import Enemy


class EntityMediator:

  @staticmethod
  def __verify_collision_window(ent: Entity):
    if isinstance(ent, Enemy):
      if ent.rect.right < 0:
        ent.health = 0

  @staticmethod
  def __verify_collision_entity(ent1, ent2):
    valid_interaction = False
    if isinstance(ent1, Enemy) and isinstance(ent2, Player):
      valid_interaction = True
    if isinstance(ent1, Player) and isinstance(ent2, Enemy):
      valid_interaction = True
    if isinstance(ent1, Player) and isinstance(ent2, Background):
      valid_interaction = True
    if isinstance(ent1, Background) and isinstance(ent2, Player):
      valid_interaction = True

    if valid_interaction:
      if (ent1.rect.right >= ent2.rect.left
          and ent1.rect.left <= ent2.rect.right
          and ent1.rect.top <= ent2.rect.bottom
          and ent1.rect.bottom >= ent2.rect.top):
        ent1.health -= ent2.damage
        ent2.health -= ent1.damage
        ent1.last_dmg = ent2.name
        ent2.last_dmg = ent1.name

  @staticmethod
  def __give_score(enemy: Enemy, entity_list: list[Entity]):
    if enemy.last_dmg == 'Player1Shoot':
      for ent in entity_list:
        if ent.name == 'Player1':
          ent.score += enemy.score

    elif enemy.last_dmg == 'Player2Shoot':
      for ent in entity_list:
        if ent.name == 'Player2':
          ent.score += enemy.score

  @staticmethod
  def verify_collision(entity_list: list[Entity]):
    for i in range(len(entity_list)):
      entity1 = entity_list[i]
      EntityMediator.__verify_collision_window(entity1)
      for j in range(i + 1, len(entity_list)):
        entity2 = entity_list[j]
        EntityMediator.__verify_collision_entity(entity1, entity2)

  @staticmethod
  def verify_health(entity_list: list[Entity]):
    # Create a new list without dead entities
    return [ent for ent in entity_list if ent.health > 0]

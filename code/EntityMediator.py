from code.Player import Player
from code.Const import WIN_HEIGHT
from code.Entity import Entity
from code.Enemy import Enemy


class EntityMediator:

  @staticmethod
  def __verify_collision_window(ent: Entity):
    if isinstance(ent, Enemy):
      if ent.rect.top > WIN_HEIGHT:
        ent.health = 0

  @staticmethod
  def __verify_collision_entity(ent1, ent2):
    valid_interaction = False
    if isinstance(ent1, Enemy) and isinstance(ent2, Player):
      valid_interaction = True
    if isinstance(ent1, Player) and isinstance(ent2, Enemy):
      valid_interaction = True

    if valid_interaction:
      overlap_x = min(ent1.rect.right, ent2.rect.right) - max(
          ent1.rect.left, ent2.rect.left)
      overlap_y = min(ent1.rect.bottom, ent2.rect.bottom) - max(
          ent1.rect.top, ent2.rect.top)

      if overlap_x > 15 and overlap_y > 15:
        if ent1.damage_cooldown <= 0 and ent2.damage_cooldown <= 0:
          ent1.health -= ent2.damage
          ent2.health -= ent1.damage
          ent1.last_dmg = ent2.name
          ent2.last_dmg = ent1.name
          ent1.damage_cooldown = 30
          ent2.damage_cooldown = 30
          
          # Lose points on collision (only players lose points)
          if isinstance(ent1, Player):
            ent1.score = max(0, ent1.score - 20)  # Lose 20 points, minimum 0
          if isinstance(ent2, Player):
            ent2.score = max(0, ent2.score - 20)  # Lose 20 points, minimum 0

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
    for ent in entity_list:
      if ent.health <= 0:
        entity_list.remove(ent)

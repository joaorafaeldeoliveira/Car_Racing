from code.Player import Player
from code.Const import WIN_HEIGHT
from code.Entity import Entity
from code.Enemy import Enemy
from code.Background import Background


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
    
    # Add background collision for dangerous background tiles
    dangerous_backgrounds = ['Level1Bg1', 'Level1Bg2', 'Level2Bg1', 'Level2Bg2']
    if isinstance(ent1, Background) and isinstance(ent2, Player) and ent1.name in dangerous_backgrounds:
      valid_interaction = True
    if isinstance(ent1, Player) and isinstance(ent2, Background) and ent2.name in dangerous_backgrounds:
      valid_interaction = True

    if valid_interaction:
      overlap_x = min(ent1.rect.right, ent2.rect.right) - max(
          ent1.rect.left, ent2.rect.left)
      overlap_y = min(ent1.rect.bottom, ent2.rect.bottom) - max(
          ent1.rect.top, ent2.rect.top)

      if overlap_x > 15 and overlap_y > 15:
        # Handle background collision differently
        if (isinstance(ent1, Background) and isinstance(ent2, Player)) or \
           (isinstance(ent1, Player) and isinstance(ent2, Background)):
          player = ent1 if isinstance(ent1, Player) else ent2
          background = ent1 if isinstance(ent1, Background) else ent2
          
          # Only damage player if they're not on cooldown and background is dangerous
          if player.damage_cooldown <= 0 and background.name in dangerous_backgrounds:
            player.health -= background.damage
            player.last_dmg = background.name
            player.damage_cooldown = 30
            player.score = max(0, player.score - 15)  # Lose 15 points for background damage
            
        # Handle player vs enemy collision  
        elif (isinstance(ent1, Enemy) and isinstance(ent2, Player)) or \
             (isinstance(ent1, Player) and isinstance(ent2, Enemy)):
          if ent1.damage_cooldown <= 0 and ent2.damage_cooldown <= 0:
            ent1.health -= ent2.damage
            ent2.health -= ent1.damage
            ent1.last_dmg = ent2.name
            ent2.last_dmg = ent1.name
            ent1.damage_cooldown = 30
            ent2.damage_cooldown = 30
            
            # Lose points on enemy collision (only players lose points)
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

from code.Entity import Entity
from code.Player import Player
from code.Enemy import Enemy
from code.Animal import Animal

class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):

        if isinstance(ent, Enemy):
            if ent.rect.right <= 0:
                pass

    @staticmethod
    def __verify_collision_entity(ent1: Entity, ent2: Entity):
        if ent1.rect.colliderect(ent2.rect):
            if isinstance(ent1, Player):
                if isinstance(ent2, Animal):
                    ent1.score += 10  # Comer animal dá pontos
                    ent2.health = 0  # Remove animal
                elif isinstance(ent2, Enemy):
                    ent1.health -= ent2.damage  # Player perde vida
                    ent1.score = max(0, ent1.score - 5)  # Player perde pontos
                    ent2.last_dmg = ent1.name
            elif isinstance(ent2, Player):
                if isinstance(ent1, Animal):
                    ent2.score += 10
                    ent1.health = 0
                elif isinstance(ent1, Enemy):
                    ent2.health -= ent1.damage
                    ent2.score = max(0, ent2.score - 5)
                    ent1.last_dmg = ent2.name

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            ent1 = entity_list[i]
            EntityMediator.__verify_collision_window(ent1)
            for j in range(i + 1, len(entity_list)):
                ent2 = entity_list[j]
                EntityMediator.__verify_collision_entity(ent1, ent2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list[:]:
            if ent.health <= 0:
                if not isinstance(ent, Enemy):
                    entity_list.remove(ent)
                else:
                    ent.health = 1

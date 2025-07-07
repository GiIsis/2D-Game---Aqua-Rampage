from code.Entity import Entity
from code.Const import ENTITY_SPEED, ENTITY_HEALTH, ENTITY_DAMAGE, ENTITY_SCORE


class Animal(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.health = ENTITY_HEALTH[name]
        self.damage = ENTITY_DAMAGE[name]
        self.score = ENTITY_SCORE[name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

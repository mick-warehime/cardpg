import logging
from random import randint

from actions.action import Action
from actions.action_type import ActionType
from actors.actor import Actor


class RandomDamage(Action):

    # 2d6+3 -> dice_faces=6, dice_count=2, modifier=3
    def __init__(self, name: str, dice_count: int, dice_faces: int, modifier: int) -> None:
        super().__init__(action_type=ActionType.DAMAGE)
        self.name = name
        self.dice_faces = dice_faces
        self.dice_count = dice_count
        self.modifier = modifier

    def act(self, actor: Actor, target: Actor) -> None:
        damage = self.get_random_damage()
        logging.info(
            '{} damage ({}d{}+{}) = {}'.format(self.name,
                                               self.dice_count,
                                               self.dice_faces,
                                               self.modifier, damage))
        target.hp = target.hp - damage

    def get_random_damage(self) -> int:
        damage = 0
        for _ in range(self.dice_count):
            damage += randint(1, self.dice_faces)
        return damage + self.modifier

from typing import Tuple
from actions.random_damage import RandomDamage
from cards.card import Card


class BluntWeapon(Card):

    def __init__(self, name: str, sprite: Tuple[int, int], dice_count: int, dice_faces: int, modifier: int) -> None:
        actions = [RandomDamage(name, dice_count, dice_faces, modifier)]
        text = 'BluntWeapon: {}d{}+{}'.format(dice_count, dice_faces, modifier)
        super().__init__(name=name, sprite=sprite, text=text, actions=actions)

from actions.random_damage import RandomDamage
from cards.card import Card


class BluntWeapon(Card):

    def __init__(self, name: str, dice_faces: int, dice_count: int, modifier: int) -> None:
        actions = [RandomDamage(name, dice_count, dice_faces, modifier)]
        super().__init__(actions=actions)

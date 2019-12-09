from typing import List

from cards.blunt_weapon import BluntWeapon
from cards.card import Card
from items.item import Item
from items.item_rarity import ItemRarity
from items.item_type import ItemType


class Mace(Item):
    N_DICE = 1
    N_SIDES = 6
    MOD = 1

    def __init__(self) -> None:
        super().__init__(name='mace', item_type=ItemType.WEAPON, rarity=ItemRarity.COMMON)

    def common_cards(self) -> List[Card]:
        return [BluntWeapon(self.name, dice_count=Mace.N_DICE, dice_faces=Mace.N_SIDES, modifier=Mace.MOD),
                BluntWeapon(self.name, dice_count=Mace.N_DICE, dice_faces=Mace.N_SIDES, modifier=Mace.MOD)]

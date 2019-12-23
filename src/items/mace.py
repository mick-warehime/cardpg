from typing import List

from cards.blunt_weapon import BluntWeapon
from cards.card import Card
from items.item import Item
from items.item_names import ItemNames
from items.item_rarity import ItemRarity
from items.item_type import ItemType


class Mace(Item):
    N_DICE = 1
    N_SIDES = 6
    MOD = 1
    N_CARDS = 8
    SPRITE = (9, 5)

    def __init__(self) -> None:
        super().__init__(item_name=ItemNames.MACE,
                         item_type=ItemType.WEAPON,
                         rarity=ItemRarity.COMMON)

    def common_cards(self) -> List[Card]:
        return [self.card() for _ in range(Mace.N_CARDS)]

    def card(self) -> Card:
        return BluntWeapon(self.name,
                           Mace.SPRITE,
                           dice_count=Mace.N_DICE,
                           dice_faces=Mace.N_SIDES,
                           modifier=Mace.MOD)

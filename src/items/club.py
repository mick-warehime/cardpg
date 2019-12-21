from typing import List

from cards.blunt_weapon import BluntWeapon
from cards.card import Card
from items.item import Item
from items.item_names import ItemNames
from items.item_rarity import ItemRarity
from items.item_type import ItemType


class Club(Item):
    N_DICE = 1
    N_SIDES = 4
    MOD = 1
    SPRITE = (8, 5)

    def __init__(self) -> None:
        super().__init__(item_name=ItemNames.CLUB,
                         item_type=ItemType.WEAPON,
                         rarity=ItemRarity.COMMON)

    def common_cards(self) -> List[Card]:
        return [BluntWeapon(self.name,
                            Club.SPRITE,
                            dice_count=Club.N_DICE,
                            dice_faces=Club.N_SIDES,
                            modifier=Club.MOD)]

from typing import List

from cards.card import Card
from items.item_rarity import ItemRarity
from items.item_type import ItemType


class Item(object):

    def __init__(self, name: str, item_type: ItemType, rarity: ItemRarity) -> None:
        self.name = name
        self.item_type = item_type
        self.rarity = rarity

    def grants_cards(self) -> List[Card]:
        if self.rarity == ItemRarity.COMMON:
            return self.common_cards()
        elif self.rarity == ItemRarity.RARE:
            return self.rare_cards()
        elif self.rarity == ItemRarity.LEGENDARY:
            return self.legendary_cards()
        else:
            return self.mythic_cards()

    def common_cards(self) -> List[Card]:
        raise NotImplementedError('Card with common rarity must implement this method')

    def rare_cards(self) -> List[Card]:
        raise NotImplementedError('Card with rare rarity must implement this method')

    def legendary_cards(self) -> List[Card]:
        raise NotImplementedError('Card with legendary rarity must implement this method')

    def mythic_cards(self) -> List[Card]:
        raise NotImplementedError('Card with mythic rarity must implement this method')

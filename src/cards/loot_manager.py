from pygame.rect import Rect

from cards.card_manager import CardManager
from cards.card_position import loot_rect


class LootManager(CardManager):

    def __init__(self, cards) -> None:
        super().__init__(cards=cards)

    def card_rect(self, index: int) -> Rect:
        return loot_rect(index, len(self.cards))

    def n_displayed(self) -> int:
        return len(self.cards)

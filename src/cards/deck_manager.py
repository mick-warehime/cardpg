from random import shuffle
from typing import List

from pygame.rect import Rect

from cards.card import Card
from cards.card_manager import CardManager
from cards.card_position import card_rect


class DeckManager(CardManager):

    def __init__(self, deck: List[Card], hand_size: int = 5) -> None:
        super().__init__(cards=deck)
        self.hand_size = min(hand_size, len(self.cards))
        self.draw_pile: List[Card] = []
        self.hand: List[Card] = []
        self.discard: List[Card] = []
        self.card_rects: List[Rect] = []
        self.selected_index = CardManager.NONE_SELECTED
        self.shuffle()

    def shuffle(self) -> None:
        self.draw_pile = self.cards.copy()
        shuffle(self.draw_pile)
        self.hand = self.draw_pile[:self.hand_size]
        self.draw_pile = self.draw_pile[self.hand_size:]
        self.discard = []
        self.update_hand()

    def update_hand(self) -> None:
        hand_size = len(self.hand)
        self.card_rects = [self.card_rect(i) for i in range(hand_size)]
        if hand_size < 1:
            self.shuffle()

    def card_rect(self, index: int) -> Rect:
        return card_rect(index, len(self.hand))

    def play_selected_card(self) -> Card:
        if self.selected_index != CardManager.NONE_SELECTED:
            card = self.hand.pop(self.selected_index)
            self.discard.append(card)
            self.selected_index = CardManager.NONE_SELECTED
            self.update_hand()
            return card
        else:
            return None

    def n_displayed(self) -> int:
        return len(self.hand)

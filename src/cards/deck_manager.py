from random import shuffle
from typing import List

from pygame.rect import Rect

from cards.card import Card
from cards.card_position import card_rect
from events.event import Event
from events.event_listener import EventListener
from events.event_type import EventType

NONE_SELECTED = -1


class DeckManager(EventListener):

    def __init__(self, deck: List[Card], hand_size: int = 5) -> None:
        super().__init__()
        self.deck = deck
        self.hand_size = min(hand_size, len(self.deck))
        self.draw_pile: List[Card] = []
        self.hand: List[Card] = []
        self.discard: List[Card] = []
        self.card_rects: List[Rect] = []
        self.selected_index = NONE_SELECTED
        self.shuffle()

    def notify(self, event: Event) -> None:
        if event.event_type == EventType.MOUSE_CLICK:
            new_selected_index = self.find_selected_index(event.x, event.y)
            if self.selected_index != new_selected_index:
                self.selected_index = new_selected_index
            else:
                self.selected_index = NONE_SELECTED

    def find_selected_index(self, x: int, y: int) -> int:
        for i in range(len(self.hand)):
            rect = self.card_rects[i]
            if rect.collidepoint(x, y):
                return i
        return NONE_SELECTED

    def shuffle(self) -> None:
        self.draw_pile = self.deck.copy()
        shuffle(self.draw_pile)
        self.hand = self.draw_pile[:self.hand_size]
        self.draw_pile = self.draw_pile[self.hand_size:]
        self.discard = []
        self.update_rects()

    def update_rects(self) -> None:
        hand_size = len(self.hand)
        self.card_rects = [card_rect(i, hand_size) for i in range(hand_size)]

    def is_selected(self, index: int) -> bool:
        return index == self.selected_index

    def selected_card(self) -> Card:
        if self.selected_index != NONE_SELECTED:
            card = self.hand.pop(self.selected_index)
            self.selected_index = NONE_SELECTED
            self.update_rects()
            return card
        else:
            return None

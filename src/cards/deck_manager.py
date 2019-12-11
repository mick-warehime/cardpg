import logging
from typing import List
from cards.card import Card
from cards.card_position import card_rect
from events.event import Event
from events.event_type import EventType
from events.event_listener import EventListener
from pygame.rect import Rect
from random import shuffle


class DeckManager(EventListener):

    def __init__(self, deck: List[Card], hand_size: int = 5) -> None:
        super().__init__()
        self.deck = deck
        self.hand_size = min(hand_size, len(self.deck))
        self.draw_pile: List[Card] = []
        self.hand: List[Card] = []
        self.discard: List[Card] = []
        self.card_rects: List[Rect] = []
        self.selected = -1
        self.shuffle()

    def notify(self, event: Event) -> None:
        if event.event_type == EventType.MOUSE_MOVE:
            for i in range(self.hand_size):
                rect = self.card_rects[i]
                if rect.collidepoint(event.x, event.y):
                    self.selected = i
                    break
                else:
                    self.selected = -1

    def shuffle(self) -> None:
        self.draw_pile = self.deck.copy()
        shuffle(self.draw_pile)
        self.hand = self.draw_pile[:self.hand_size]
        self.draw_pile = self.draw_pile[self.hand_size:]
        self.discard = []
        self.card_rects = [card_rect(i, self.hand_size) for i in range(self.hand_size)]

    def is_selected(self, index: int) -> bool:
        return index == self.selected

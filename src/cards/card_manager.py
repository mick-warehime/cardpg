import abc
from typing import List

from pygame.rect import Rect

from cards.card import Card
from events.event import Event
from events.event_listener import EventListener
from events.event_type import EventType


class CardManager(EventListener):
    NONE_SELECTED = -1

    def __init__(self, cards: List[Card]) -> None:
        super().__init__()
        self.cards = cards
        self.selected_index = CardManager.NONE_SELECTED

    def notify(self, event: Event) -> None:
        if event.event_type == EventType.MOUSE_CLICK:
            new_selected_index = self.find_selected_index(event.x, event.y)
            if self.selected_index != new_selected_index:
                self.selected_index = new_selected_index
            else:
                self.selected_index = CardManager.NONE_SELECTED

    def find_selected_index(self, x: int, y: int) -> int:
        for i in range(self.n_displayed()):
            rect = self.card_rect(i)
            if rect.collidepoint(x, y):
                return i
        return CardManager.NONE_SELECTED

    def is_selected(self, index: int) -> bool:
        return index == self.selected_index

    @abc.abstractmethod
    def card_rect(self, index: int) -> Rect:
        pass

    @abc.abstractmethod
    def n_displayed(self) -> int:
        # number of cards to display
        pass

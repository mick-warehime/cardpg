from events.event import Event
from events.event_type import EventType


class AddCardEvent(Event):
    def __init__(self, card: 'Card') -> None:
        Event.__init__(self, EventType.ADD_CARD)
        self.card = card

    def __str__(self) -> str:
        return 'add card {}'.format(self.card)

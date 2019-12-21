from events.event import Event
from events.event_type import EventType


class PlayCardEvent(Event):
    def __init__(self, card: 'Card') -> None:
        Event.__init__(self, EventType.PLAY_CARD)
        self.card = card

    def __str__(self) -> str:
        return 'card {}'.format(self.card)

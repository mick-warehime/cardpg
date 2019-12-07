from events.event import Event
from events.event_type import EventType


class ChangeScreenEvent(Event):
    def __init__(self, next_screen: str) -> None:
        Event.__init__(self, EventType.CHANGE_SCREEN)
        self.next_screen = next_screen

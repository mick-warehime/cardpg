from events.event import Event
from events.event_type import EventType


class KeyPressEvent(Event):
    def __init__(self, key: str, pressed: bool) -> None:
        Event.__init__(self, EventType.KEY_PRESS)
        self.key = key
        self.pressed = pressed

    def __str__(self) -> str:
        return 'key=%s pressed=%s' % (self.key, self.pressed)

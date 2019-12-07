from typing import Tuple
from events.event import Event
from events.event_type import EventType


class MouseClickEvent(Event):
    def __init__(self, pressed: bool, position: Tuple[int, int]) -> None:
        Event.__init__(self, EventType.MOUSE_CLICK)
        self.pressed = pressed
        self.position = position

    def __str__(self) -> str:
        return 'pressed=%s, pos:%s' % (self.pressed, self.position)

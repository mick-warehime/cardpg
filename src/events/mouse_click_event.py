from events.event import Event
from events.event_type import EventType


class MouseClickEvent(Event):
    def __init__(self, pressed: bool, x: int, y: int) -> None:
        Event.__init__(self, EventType.MOUSE_CLICK)
        self.pressed = pressed
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return 'pressed=%s, pos:(%s, %s)' % (self.pressed, self.x, self.y)

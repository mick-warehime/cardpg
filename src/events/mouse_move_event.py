from events.event import Event
from events.event_type import EventType


class MouseMoveEvent(Event):
    def __init__(self, x: int, y: int) -> None:
        Event.__init__(self, EventType.MOUSE_MOVE)
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return '(mouse move: ({}, {}))'.format(self.x, self.y)

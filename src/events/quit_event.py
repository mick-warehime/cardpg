from events.event import Event
from events.event_type import EventType


class QuitEvent(Event):
    def __init__(self):
        Event.__init__(self, EventType.QUIT)

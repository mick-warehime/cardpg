from events.event import Event
from events.event_type import EventType


class TickEvent(Event):
    def __init__(self):
        Event.__init__(self, EventType.TICK)

from events.event_type import EventType


class Event(object):
    def __init__(self, event_type: EventType) -> None:
        self.event_type = event_type

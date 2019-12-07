from events.event import Event
from events.event_listener import EventListener


class Model(EventListener):
    def __init__(self) -> None:
        super(Model, self).__init__()

    def notify(self, event: Event) -> None:
        pass

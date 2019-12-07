import abc
from events.event_manager import EventManager
from event import Event


class EventListener(metaclass=abc.ABCMeta):

    def __init__(self) -> None:
        EventManager.register(self)

    @abc.abstractmethod
    def notify(self, event: Event) -> None:
        """Notify the listener of an event."""
        pass

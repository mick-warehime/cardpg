import abc

from events.event import Event
from events.event_manager import EventManager


class EventListener(metaclass=abc.ABCMeta):

    def __init__(self) -> None:
        EventManager.register(self)

    @abc.abstractmethod
    def notify(self, event: Event) -> None:
        """Notify the listener of an event."""
        pass

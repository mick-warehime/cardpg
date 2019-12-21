import abc

from events.event import Event
from events.event_manager import EventManager
from events.event_priority import EventPriority


class EventListener(metaclass=abc.ABCMeta):

    def __init__(self, priority=EventPriority.LAST) -> None:
        self._priority = priority
        EventManager.register(self)

    @abc.abstractmethod
    def notify(self, event: Event) -> None:
        """Notify the listener of an event."""
        pass

    @property
    def priority(self) -> EventPriority:
        return self._priority

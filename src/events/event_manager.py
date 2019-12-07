import logging
from weakref import WeakSet

from events.event import Event
from events.event_type import EventType


class EventManager(object):
    listeners = WeakSet()

    @classmethod
    def register(cls, l: 'EventListener') -> None:
        cls.listeners.add(l)
        logging.debug('registered listener {0} {1}'.format(
            len(cls.listeners), l))

    @classmethod
    def post(cls, event: Event) -> None:
        if event.event_type != EventType.TICK:
            logging.debug('EVENT: {}'.format(str(event)))

        for l in cls.listeners.copy():
            l.notify(event)

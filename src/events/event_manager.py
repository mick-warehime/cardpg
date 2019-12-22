import logging
from weakref import WeakSet

from events.event import Event
from events.event_type import EventType

IGNORED_EVENTS = set([EventType.TICK, EventType.MOUSE_MOVE])


class EventManager(object):
    listeners = WeakSet()

    @classmethod
    def register(cls, l: 'EventListener') -> None:
        cls.listeners.add(l)
        logging.debug('registered listener {0} {1}'.format(
            len(cls.listeners), l))

    @classmethod
    def post(cls, event: Event) -> None:
        if event.event_type not in IGNORED_EVENTS:
            logging.debug('EVENT: {}'.format(str(event)))

        # TODO - SORTS LISTENERS EVERY EVENT!!! Need to find a better way to destory listeners
        # and then we can keep a sorted list here instead of a weakset
        for l in sorted(cls.listeners, key=lambda x: x.priority).copy():
            l.notify(event)

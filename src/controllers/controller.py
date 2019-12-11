import abc

from events.event import Event
from events.event_type import EventType
from events.event_listener import EventListener
from models.model import Model
from views.view import View

IGNORED_EVENTS = set([EventType.TICK, EventType.MOUSE_MOVE])


class Controller(EventListener):

    def __init__(self, model: Model, view: View) -> None:
        super().__init__()
        self._model = model
        self._view = view
        self.initial_draw = False

    def notify(self, event: Event) -> None:
        if event.event_type not in IGNORED_EVENTS or not self.initial_draw:
            self.update(event)
            self._view.update(self._model)

        if not self.initial_draw:
            self.initial_draw = True

    @abc.abstractmethod
    def update(self, event: Event) -> None:
        pass

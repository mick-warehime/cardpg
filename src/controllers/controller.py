import abc
from events.event_listener import EventListener
from events.event import Event
from models.model import Model
from views.view import View


class Controller(EventListener):

    def __init__(self, model: Model, view: View) -> None:
        super(Controller, self).__init__()
        self._model = model
        self._view = view

    def notify(self, event: Event) -> None:
        self.update(event)
        self._view.update(self._model)

    @abc.abstractmethod
    def update(self, event: Event) -> None:
        pass

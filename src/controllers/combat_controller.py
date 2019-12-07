from controllers.controller import Controller
from events.event import Event
from events.event import EventType
from events.event_manager import EventManager
from events.change_screen_event import ChangeScreenEvent


class CombatController(Controller):
    def update(self, event: Event) -> None:
        if event.event_type == EventType.KEY_PRESS:
            if event.key == 'x':
                EventManager.post(ChangeScreenEvent('settings'))

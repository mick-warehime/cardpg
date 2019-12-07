from controllers.controller import Controller
from events.change_screen_event import ChangeScreenEvent
from events.event import Event, EventType
from events.event_manager import EventManager


class SettingsController(Controller):
    def update(self, event: Event) -> None:
        if event.event_type == EventType.KEY_PRESS:
            if event.key == 'y':
                EventManager.post(ChangeScreenEvent('combat'))

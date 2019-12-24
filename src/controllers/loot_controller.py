from controllers.controller import Controller
from events.add_card_event import AddCardEvent
from events.change_screen_event import ChangeScreenEvent
from events.event import Event, EventType
from events.event_manager import EventManager


class LootController(Controller):

    def update(self, event: Event) -> None:
        if event.event_type == EventType.KEY_PRESS:
            if event.key == 'x':
                EventManager.post(ChangeScreenEvent('settings'))

            if event.key == 'a':
                self.loot()

    def loot(self) -> None:
        card = self._model.selected_card()
        if card:
            EventManager.post(AddCardEvent(card))
            EventManager.post(ChangeScreenEvent('combat'))

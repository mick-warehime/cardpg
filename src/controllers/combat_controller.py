import logging

from controllers.controller import Controller
from events.change_screen_event import ChangeScreenEvent
from events.event import Event, EventType
from events.event_manager import EventManager
from models.combat_model import CombatModel
from views.combat_view import CombatView


class CombatController(Controller):

    def __init__(self, model: CombatModel, view: CombatView) -> None:
        super().__init__(model, view)
        self._model = model
        self._view = view

    def update(self, event: Event) -> None:
        if event.event_type == EventType.KEY_PRESS:
            if event.key == 'x':
                EventManager.post(ChangeScreenEvent('settings'))

            if event.key == 'a':
                self.attack()

                if self._model.skeleton.hp <= 0:
                    EventManager.post(ChangeScreenEvent('loot', actor=self._model.skeleton))

    def attack(self) -> None:
        char = self._model.character
        skel = self._model.skeleton

        card = self._model.play_selected_card()
        if card:
            logging.info('cn: {}, sk: {}'.format(char.hp, skel.hp))
            card.play(char, skel)
            skel.cards()[0].play(skel, char)
            logging.info('cn: {}, sk: {}'.format(char.hp, skel.hp))

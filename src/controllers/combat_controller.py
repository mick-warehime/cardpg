import logging

from controllers.controller import Controller
from events.change_screen_event import ChangeScreenEvent
from events.event import Event, EventType
from events.event_manager import EventManager


class CombatController(Controller):

    def update(self, event: Event) -> None:
        if event.event_type == EventType.KEY_PRESS:
            if event.key == 'x':
                EventManager.post(ChangeScreenEvent('settings'))

            if event.key == 'a':
                self.attack()
        if event.event_type == EventType.PLAY_CARD:
            # TODO - remove card from hand
            logging.info('played card')

    def attack(self) -> None:
        char = self._model.character
        skel = self._model.skeleton
        logging.info('cn: {}, sk: {}'.format(char.hp, skel.hp))

        char.cards()[0].play(char, skel)
        skel.cards()[0].play(skel, char)

        logging.info('cn: {}, sk: {}'.format(char.hp, skel.hp))

import os
import sys
from typing import Optional

import pygame

from controller_factory import build_controller
from controllers.keyboard import Keyboard
from data import constants
from events.event import Event
from events.event_listener import EventListener
from events.event_manager import EventManager
from events.event_type import EventType
from events.tick_event import TickEvent


def initialize_pygame(no_ui: bool = False) -> None:
    if no_ui:
        os.environ['SDL_VIDEODRIVER'] = 'dummy'
        os.environ['SDL_AUDIODRIVER'] = 'dummy'

    pygame.mixer.pre_init(44100, -16, 4, 2048)
    pygame.init()
    pygame.font.init()


class Game(EventListener):
    """Stores sceneMachine and keyboard, handles framerate and quit event."""
    keyboard: Optional[Keyboard] = None

    def __init__(self) -> None:
        super().__init__()
        self.clock: pygame.Clock = pygame.time.Clock()
        self.keyboard = Keyboard()
        self.controller = build_controller('combat')

    def notify(self, event: Event) -> None:
        if event.event_type == EventType.QUIT:
            pygame.quit()
            sys.exit()
        elif event.event_type == EventType.TICK:
            # limits the redraw speed
            self.clock.tick(constants.FRAMES_PER_SECOND)
        elif event.event_type == EventType.CHANGE_SCREEN:
            self.controller = build_controller(event.next_screen)

    def run(self) -> None:
        while True:
            EventManager.post(TickEvent())

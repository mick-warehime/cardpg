import pygame

from events.event import Event
from events.event_listener import EventListener
from events.event_manager import EventManager
from events.key_press_event import KeyPressEvent
from events.mouse_click_event import MouseClickEvent
from events.mouse_move_event import MouseMoveEvent
from events.quit_event import QuitEvent
from events.tick_event import TickEvent


class Keyboard(EventListener):
    def __init__(self) -> None:
        super().__init__()

    def notify(self, event: Event) -> None:
        if isinstance(event, TickEvent):
            self.handle_inputs()

    def handle_inputs(self) -> None:
        # Called for each game tick. We check our keyboard presses here.
        for pg_event in pygame.event.get():
            # handle window manager closing our window
            if self.is_quit_event(pg_event):
                EventManager.post(QuitEvent())
            # handle key down events
            elif pg_event.type == pygame.KEYDOWN:
                self.handle_keypress(pg_event.unicode, pressed=True)
            # elif pg_event.type == pygame.KEYUP:
            #     self.handle_keypress(pg_event.unicode, pressed=False)
            elif pg_event.type == pygame.MOUSEBUTTONDOWN:
                self.handle_mouse_click(pressed=True)
            # Not needed so far.
            # elif pg_event.type == pygame.MOUSEBUTTONUP:
            #     self.handle_mouse_click(pressed=False)
            # This makes things slow
            # elif pg_event.type == pygame.MOUSEMOTION:
            #     self.handle_mouse_motion()

    def handle_keypress(self, key_name: str, pressed: bool) -> None:
        input_event = KeyPressEvent(key=key_name, pressed=pressed)
        EventManager.post(input_event)

    def handle_mouse_click(self, pressed: bool) -> None:
        x, y = pygame.mouse.get_pos()
        mouse_event = MouseClickEvent(x=x, y=y, pressed=pressed)
        EventManager.post(mouse_event)

    def handle_mouse_motion(self) -> None:
        x, y = pygame.mouse.get_pos()
        mouse_move_event = MouseMoveEvent(x, y)
        EventManager.post(mouse_move_event)

    def get_binding(self, key: str) -> Event:
        return self.bindings.event_for_key(key)

    def is_quit_event(self, pg_event: pygame.event.EventType) -> bool:
        if pg_event.type == pygame.QUIT:
            return True
        return pg_event.type == pygame.KEYDOWN and pg_event.key == pygame.K_ESCAPE

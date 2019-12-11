from enum import Enum


class EventType(Enum):
    TICK = 1
    QUIT = 2
    MOUSE_CLICK = 3
    KEY_PRESS = 4
    CHANGE_SCREEN = 5
    PLAY_CARD = 6

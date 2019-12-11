from enum import Enum


class EventType(Enum):
    CHANGE_SCREEN = 1
    KEY_PRESS = 2
    MOUSE_CLICK = 3
    MOUSE_MOVE = 4
    PLAY_CARD = 5
    QUIT = 6
    TICK = 7

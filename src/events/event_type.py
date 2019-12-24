from enum import Enum


class EventType(Enum):
    CHANGE_SCREEN = 1
    KEY_PRESS = 2
    MOUSE_CLICK = 3
    MOUSE_MOVE = 4
    PLAY_CARD = 5
    ADD_CARD = 6
    QUIT = 7
    TICK = 8

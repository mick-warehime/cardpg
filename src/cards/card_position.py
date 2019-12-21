from pygame.rect import Rect

from data.constants import (CARD_FROM_BOTTOM, CARD_HEIGHT, CARD_SPACE,
                            CARD_WIDTH, SCREEN_SIZE)


def card_position(index: int, hand_size: int):
    y = SCREEN_SIZE[1] - CARD_FROM_BOTTOM - CARD_HEIGHT
    screen_width = SCREEN_SIZE[0]
    hand_width = hand_size * CARD_WIDTH + (hand_size - 1) * CARD_SPACE
    first_card_x = (screen_width - hand_width) / 2
    x = first_card_x + (CARD_WIDTH + CARD_SPACE) * index
    return x, y


def card_rect(index: int, hand_size: int) -> Rect:
    x, y = card_position(index, hand_size)
    return Rect(x, y, CARD_WIDTH, CARD_HEIGHT)

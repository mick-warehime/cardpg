from data.constants import SCREEN_SIZE
from data.constants import CARD_FROM_BOTTOM
from data.constants import CARD_HEIGHT
from data.constants import CARD_WIDTH
from data.constants import CARD_SPACE


def card_position(index: int, hand_size: int):
    y = SCREEN_SIZE[1] - CARD_FROM_BOTTOM - CARD_HEIGHT
    screen_width = SCREEN_SIZE[0]
    hand_width = hand_size * CARD_WIDTH + (hand_size - 1) * CARD_SPACE
    first_card_x = (screen_width - hand_width) / 2
    x = first_card_x + (CARD_WIDTH + CARD_SPACE) * index
    return (x, y)

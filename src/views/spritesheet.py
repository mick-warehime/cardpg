from typing import Tuple

import pygame
from pygame import Rect

SHEET = None
SPRITES_FILE_PATH = 'src/assets/sprites.png'
SPRITE_WIDTH = 48
SPRITE_HEIGHT = 48


def sheet():
    global SHEET

    if not SHEET:
        SHEET = pygame.image.load(SPRITES_FILE_PATH).convert()

    return SHEET


# Load a specific image from a specific rectangle
def image_at(rectangle: Rect, color_key=None):
    rect = pygame.Rect(rectangle)
    image = pygame.Surface(rect.size).convert()
    image.blit(sheet(), (0, 0), rect)
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key, pygame.RLEACCEL)
    return image


def load_sprite_at(sprite: Tuple[int, int]) -> pygame.Surface:
    col = sprite[0]
    row = sprite[1]
    rect = Rect(col * SPRITE_WIDTH,
                row * SPRITE_HEIGHT,
                SPRITE_WIDTH,
                SPRITE_HEIGHT)
    return image_at(rect)

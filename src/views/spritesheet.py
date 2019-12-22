from typing import Tuple

import pygame
from pygame import Rect

SHEETS = {}
SPRITES_FILE_PATH = 'src/assets/sprites.png'
ENEMIES_FILE_PATH = 'src/assets/enemies.png'
CHARACTER_FILE_PATH = 'src/assets/characters.png'
SPRITE_WIDTH = 48
SPRITE_HEIGHT = 48
ENEMY_WIDTH = 94
ENEMY_HEIGHT = 140
ENEMY_WIDTH_OFFSET = 30
ENEMY_HEIGHT_OFFSET = 24
ENEMY_W_SPACE = 11
ENEMY_H_SPACE = 4
CHARACTER_WIDTH = 32
CHARACTER_HEIGHT = 32


def laod_sheet(sheet_name: str):
    global SHEETS

    if sheet_name not in SHEETS:
        SHEETS[sheet_name] = pygame.image.load(sheet_name).convert()

    return SHEETS[sheet_name]


# Load a specific image from a specific rectangle
def image_at(rectangle: Rect, sheet_name: str, color_key=None):
    rect = pygame.Rect(rectangle)
    image = pygame.Surface(rect.size).convert()
    image.blit(laod_sheet(sheet_name), (0, 0), rect)
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
    return image_at(rect, SPRITES_FILE_PATH)


def load_enemy_at(sprite: Tuple[int, int]) -> pygame.Surface:
    col = sprite[0]
    row = sprite[1]
    rect = Rect(ENEMY_WIDTH_OFFSET + col * (ENEMY_WIDTH + ENEMY_W_SPACE),
                ENEMY_HEIGHT_OFFSET + row * (ENEMY_HEIGHT + ENEMY_H_SPACE),
                ENEMY_WIDTH,
                ENEMY_HEIGHT)
    return image_at(rect, ENEMIES_FILE_PATH)


def load_character_at(sprite: Tuple[int, int]) -> pygame.Surface:
    col = sprite[0]
    row = sprite[1]
    rect = Rect(col * CHARACTER_WIDTH,
                row * CHARACTER_WIDTH,
                CHARACTER_WIDTH,
                CHARACTER_HEIGHT)
    return image_at(rect, CHARACTER_FILE_PATH)

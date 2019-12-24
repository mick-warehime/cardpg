import os
from abc import abstractmethod
from typing import Dict, List, Tuple

import pygame
from pygame.rect import Rect
from pygame.surface import Surface

from data import constants
from data.colors import DARK_GRAY, RED, WHITE, ColorType
from data.constants import CARD_HEIGHT
from views.pygame_images import load_image
from views.spritesheet import load_character_at, load_enemy_at, load_sprite_at


class Screen(object):

    @abstractmethod
    def render_text(
            self, text: str, font_size: int, x: int, y: int,
            color: ColorType, w: int = None, h: int = None) -> Rect:
        r"""Render formatted text at a specific point on the screen.

        Multi-line text must be handled using newline characters ('\n')

        Args:
            text: Text to be rendered.
            font_size: Size of text.
            x: x coordinate of top left of text box.
            y: y coordinate of top left of text box.
            color: text color (RGB).
            w: (Optional) If passed text is centered horizontally assuming a
                rectangle with left edge at x and width w.
            h: (Optional) If passed text is centered vertically assuming a
                rectangle with top edge at y and height h.

        Returns:
            The Rect of the rendered text.
        """
        pass

    @abstractmethod
    def render_text_in_rect(self, text: str, font_size: int, rect: Rect,
                            color: ColorType, center_x: bool = False,
                            center_y: bool = False) -> None:
        r"""Render formatted text into a desired rect.

        Multi-line text is automatically broken up to fit within the rect. If
        it does not fit, the text is resized. Newline characters ('\n') are
        ignored

        Args:
            text: Text to be rendered.
            font_size: Size of text.
            rect: The rect object containing the text. The rect must be wider
                than the longest rendered word.
            color: text color (RGB).
            center_x: Whether to center the text horizontally in the rect.
            center_y: Whether to center the text vertically in the rect.
        """
        raise NotImplementedError

    @abstractmethod
    def render_image(self, image_path: str, x: int, y: int, w: int,
                     h: int) -> None:
        """Adds an image to the screen at (x, y) with width, w, and height, h.
        """
        pass

    @abstractmethod
    def render_rect(self, rect: Rect, color: ColorType, width: int) -> None:
        """Draws a rectangle onto the current screen.

        Args:
            rect: The rectangle to be drawn. Coordinates must match absolute
                screen coordinates.
            color: Fill or boundary color.
            width: Boundary width. If zero, the rect is filled.

        """

    @abstractmethod
    def clear(self) -> None:
        """Removes everything from the screen."""
        pass

    @abstractmethod
    def update(self) -> None:
        """Makes sure any render/clear calls have been posted to the screen."""
        pass

    @abstractmethod
    def render_line(self, start: Tuple[int, int], end: Tuple[int, int],
                    color: ColorType, thickness: int = 2) -> None:
        """Draw a line on the screen."""

    @abstractmethod
    def render_sprite(self, sprite: Tuple[int, int],
                      x: int,
                      y: int,
                      scale: Tuple[int, int]) -> None:
        """"Render from the items spriteshite"""

    @abstractmethod
    def render_enemy(self, sprite: Tuple[int, int],
                     x: int,
                     y: int,
                     scale: Tuple[int, int]) -> None:
        """"Render from the enemies spriteshite"""

    @abstractmethod
    def render_actor(self, sprite: Tuple[int, int],
                     x: int,
                     y: int,
                     scale: Tuple[int, int]) -> None:
        """"Render from the enemies spriteshite"""

    @abstractmethod
    def render_card(self,
                    title: str,
                    text: str,
                    rect: Rect,
                    sprite: Surface,
                    is_selected: bool) -> None:
        """"Render from the enemies spriteshite"""


class _PygameScreen(Screen):
    _screen: pygame.Surface = None
    TITLE_FONT = 30
    BODY_FONT = 20
    SPRITE_SIZE = (140, 140)

    def __init__(self) -> None:
        if self._screen is None:
            self._initialize_screen()
        self._fonts: Dict[int, pygame.font.Font] = {}

    def _font(self, size: int) -> pygame.font.Font:
        if size not in self._fonts:
            font = pygame.font.SysFont(None, size)
            self._fonts[size] = font
        else:
            font = self._fonts[size]
        return font

    def _initialize_screen(self) -> None:
        pygame.display.set_caption('6th Corp')
        try:
            self._screen = pygame.display.set_mode(constants.SCREEN_SIZE)
        except pygame.error:
            # If no video device is available, use dummy device. This is only
            # relevant in travis.
            os.environ['SDL_VIDEODRIVER'] = 'dummy'
            os.environ['SDL_AUDIODRIVER'] = 'dummy'
            self._screen = pygame.display.set_mode(constants.SCREEN_SIZE)

    def update(self) -> None:
        """Makes sure any render/clear calls have been posted to the screen."""
        pygame.display.flip()

    def render_texts(

            self,
            texts: List[str],
            font_size: int,
            x: int,
            y: int,
            color: ColorType,
            spacing: int) -> None:
        for text in texts:
            self.render_text(text, font_size, x, y, color)
            y += spacing

    def render_text(self, text: str, font_size: int, x: int, y: int,
                    color: ColorType, w: int = None, h: int = None) -> Rect:
        font = self._font(font_size)
        rasterized = font.render(text, True, color)

        kwargs = {}
        if w is None:
            kwargs['x'] = x
        else:
            kwargs['centerx'] = x + w // 2

        if h is None:
            kwargs['y'] = y
        else:
            kwargs['centery'] = y + h // 2

        rect = rasterized.get_rect(**kwargs)

        self._screen.blit(rasterized, rect)
        return rect

    def render_line(self, start: Tuple[int, int], end: Tuple[int, int],
                    color: ColorType, thickness: int = 2) -> None:
        pygame.draw.line(self._screen, color, start, end, thickness)

    def render_text_in_rect(self, text: str, font_size: int, rect: Rect,
                            color: ColorType, center_x: bool = False,
                            center_y: bool = False) -> None:
        font = self._font(font_size)

        # We break up all the text into words, then populate lines until no more
        # words can be fitted in the rect.
        words = text.split(' ')[::-1]

        lines = []
        current_line = ''
        while words:
            bigger_line = current_line + ' ' + words[-1]
            if font.size(bigger_line)[0] < rect.w:  # word can be added to line
                current_line = bigger_line
                words.pop()
            else:  # make a new line
                lines.append(current_line[1:])  # ignore first space
                assert current_line, (
                    'rect is too small to fit single word {}'.format(words[-1]))
                current_line = ''
        lines.append(current_line[1:])

        # order all line surfaces paired with the rects that contain them
        surfaces_rects: List[Tuple[pygame.Surface, Rect]] = []
        y = rect.y

        kwargs = {}
        if center_x:
            kwargs['centerx'] = rect.x + rect.w // 2
        else:
            kwargs['x'] = rect.x

        for line in lines:
            line_surf = font.render(line, True, color)

            kwargs['y'] = y

            line_rect = line_surf.get_rect(**kwargs)
            y += line_rect.h
            surfaces_rects.append((line_surf, line_rect))

        # If text does not fit in rect, decrease font and call again
        if y > rect.y + rect.h:
            self.render_text_in_rect(text, font_size - 2, rect, color, center_x,
                                     center_y)
            return

        # If y centering, shift each line down
        if center_y:
            text_height = y - rect.y
            shift = (rect.h - text_height) // 2
            for _, line_rect in surfaces_rects:
                line_rect.y += shift

        for line_surf, line_rect in surfaces_rects:
            self._screen.blit(line_surf, line_rect)

    def render_image(self, image_path: str, x: int, y: int, w: int,
                     h: int) -> None:
        image = load_image(image_path)
        rect = image.get_rect()
        rect.x = x
        rect.y = y
        if w > 0 and h > 0:
            image = pygame.transform.scale(image, (w, h))
        self._screen.blit(image, rect)

    def render_rect(self, rect: Rect, color: ColorType, width: int) -> None:
        pygame.draw.rect(self._screen, color, rect, width)

    def clear(self) -> None:
        self._screen.fill((0, 0, 0))

    def render_sprite(self, sprite: Tuple[int, int],
                      x: int,
                      y: int,
                      scale: Tuple[int, int] = None) -> None:

        sprite = load_sprite(sprite)
        self.render_surface(sprite, x, y, scale)

    def render_enemy(self, sprite: Tuple[int, int],
                     x: int,
                     y: int,
                     scale: Tuple[int, int] = None) -> None:

        enemy = load_enemy(sprite)
        self.render_surface(enemy, x, y, scale)

    def render_character(self, sprite: Tuple[int, int],
                         x: int,
                         y: int,
                         scale: Tuple[int, int] = None) -> None:

        char = load_character(sprite)
        self.render_surface(char, x, y, scale)

    def render_surface(self, surface: Surface, x: int, y: int, scale: Tuple[int, int]) -> None:
        if scale:
            sprite = pygame.transform.scale(surface, scale)
        self._screen.blit(sprite, (x, y))

    def render_card(self,
                    title: str,
                    text: str,
                    rect: Rect,
                    sprite: Surface,
                    is_selected: bool) -> None:
        self.render_rect(rect, WHITE, 0)
        self.render_text(title, _PygameScreen.TITLE_FONT, rect.x + 3, rect.y - 3, DARK_GRAY)
        self.render_text(text, _PygameScreen.BODY_FONT, rect.x + 3, rect.y + 2 * CARD_HEIGHT / 3,
                         DARK_GRAY)
        self.render_sprite(sprite, rect.x + 20, rect.y + 20, _PygameScreen.SPRITE_SIZE)

        if is_selected:
            self.render_rect(rect, RED, 2)


SPRITE_CACHE = {}


def load_sprite(sprite: Tuple[int, int]) -> Surface:
    if sprite not in SPRITE_CACHE:
        SPRITE_CACHE[sprite] = load_sprite_at(sprite)
    return SPRITE_CACHE[sprite]


def load_enemy(sprite: Tuple[int, int]) -> Surface:
    if sprite not in SPRITE_CACHE:
        SPRITE_CACHE[sprite] = load_enemy_at(sprite)
    return SPRITE_CACHE[sprite]


def load_character(sprite: Tuple[int, int]) -> Surface:
    if sprite not in SPRITE_CACHE:
        SPRITE_CACHE[sprite] = load_character_at(sprite)
    return SPRITE_CACHE[sprite]


_screen = None


def get_screen() -> Screen:
    global _screen
    if _screen is None:
        _screen = _PygameScreen()
    return _screen

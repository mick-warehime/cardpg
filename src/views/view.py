from typing import List

from artists.artist import Artist
from data.colors import GREEN
from views.pygame_screen import get_screen


class View(object):
    """Manages all drawing on the screen for a given model."""

    def __init__(self, artists: List[Artist]) -> None:
        self._artists = artists
        self._screen = get_screen()
        self._debug_mode = False

    def update(self, model) -> None:
        self._screen.clear()
        for artist in self._artists:
            artist.render(self._screen, model)
        if self._debug_mode and hasattr(model, 'layout'):
            layout = model.layout  # type: ignore
            for rect in layout.get_rects(layout):
                self._screen.render_rect(rect, GREEN, 2)

        # VERY IMPORTANT TO CALL UPDATE ONCE
        self._screen.update()

    def toggle_debug(self) -> None:
        """Toggle DEBUG mode, where all layout rects are drawn."""
        self._debug_mode = not self._debug_mode

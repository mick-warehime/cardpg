from data.colors import WHITE
from artists.drawing_utils import rescale_horizontal, rescale_vertical
from views.pygame_screen import Screen
from models.model import Model
from artists.artist import Artist


class SettingsArtist(Artist):

    def render(self, screen: Screen, model: Model) -> None:
        x, font_size, spacing = rescale_horizontal(250, 35, 50)
        y, = rescale_vertical(250)
        screen.render_text('Settings! (press y)',
                           font_size=font_size,
                           x=x,
                           y=y,
                           color=WHITE)

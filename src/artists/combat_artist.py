from artists.artist import Artist
from artists.drawing_utils import rescale_horizontal, rescale_vertical
from data.colors import WHITE
from models.model import Model
from views.pygame_screen import Screen


class CombatArtist(Artist):

    def render(self, screen: Screen, model: Model) -> None:
        x, font_size, spacing = rescale_horizontal(250, 35, 50)
        y, = rescale_vertical(250)
        screen.render_text('Combat! (press x)',
                           font_size=font_size,
                           x=x,
                           y=y,
                           color=WHITE)

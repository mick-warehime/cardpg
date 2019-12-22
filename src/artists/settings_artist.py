from artists.artist import Artist
from data.colors import WHITE
from data.constants import SCREEN_SIZE
from models.model import Model
from views.pygame_screen import Screen


class SettingsArtist(Artist):

    def render(self, screen: Screen, model: Model) -> None:
        screen.render_text('Combat: y',
                           font_size=40,
                           x=SCREEN_SIZE[0] - 200,
                           y=0,
                           color=WHITE)

from artists.artist import Artist
from data.colors import WHITE
from models.model import Model
from views.pygame_screen import Screen


class CombatArtist(Artist):

    def render(self, screen: Screen, model: Model) -> None:
        screen.render_text('Settings: x',
                           font_size=40,
                           x=0,
                           y=0,
                           color=WHITE)

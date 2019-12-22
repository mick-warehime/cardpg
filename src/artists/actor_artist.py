from artists.artist import Artist
from data.constants import SCREEN_SIZE
from models.combat_model import CombatModel
from views.pygame_screen import Screen


class ActorArtist(Artist):
    ENEMY_SCALE = 1.9
    ENEMY_SIZE = (int(90 * ENEMY_SCALE), int(140 * ENEMY_SCALE))
    CHARACTER_SCALE = 4
    CHARACTER_SIZE = (int(32 * CHARACTER_SCALE), int(32 * CHARACTER_SCALE))

    def render(self, screen: Screen, model: CombatModel) -> None:
        screen.render_enemy(model.skeleton.sprite,
                            SCREEN_SIZE[0] - 500, 200, ActorArtist.ENEMY_SIZE)
        screen.render_character(model.character.sprite, 300, 300, ActorArtist.CHARACTER_SIZE)

from artists.artist import Artist
from data.colors import WHITE
from data.constants import SCREEN_SIZE
from models.combat_model import CombatModel
from views.pygame_screen import Screen


class ActorArtist(Artist):
    ENEMY_SCALE = 1.9
    ENEMY_SIZE = (int(90 * ENEMY_SCALE), int(140 * ENEMY_SCALE))
    CHARACTER_SCALE = 4
    CHARACTER_SIZE = (int(32 * CHARACTER_SCALE), int(32 * CHARACTER_SCALE))
    ENEMY_X = SCREEN_SIZE[0] - 500
    ENEMY_Y = 200
    CHAR_X = 300
    CHAR_Y = 300

    def render(self, screen: Screen, model: CombatModel) -> None:
        enemy_life_str = '{}/{}'.format(model.skeleton.hp, model.skeleton.max_hp)
        screen.render_text(enemy_life_str, 30, ActorArtist.ENEMY_X, ActorArtist.ENEMY_Y-20, WHITE)
        screen.render_enemy(model.skeleton.sprite, ActorArtist.ENEMY_X,
                            ActorArtist.ENEMY_Y, ActorArtist.ENEMY_SIZE)

        char_life_str = '{}/{}'.format(model.character.hp, model.character.max_hp)
        screen.render_text(char_life_str, 30, ActorArtist.CHAR_X, ActorArtist.CHAR_X - 20, WHITE)
        screen.render_character(model.character.sprite, ActorArtist.CHAR_X,
                                ActorArtist.CHAR_Y, ActorArtist.CHARACTER_SIZE)

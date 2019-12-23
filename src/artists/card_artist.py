from typing import List

from pygame.rect import Rect

from artists.artist import Artist
from cards.card import Card
from cards.card_position import card_position
from data.colors import DARK_GRAY, RED, WHITE
from data.constants import CARD_HEIGHT, CARD_WIDTH, SCREEN_SIZE
from models.combat_model import CombatModel
from views.pygame_screen import Screen


class CardArtist(Artist):
    MAX_HAND_SIZE = 7
    TITLE_FONT = 30
    BODY_FONT = 20
    SPRITE_SIZE = (140, 140)

    def render(self, screen: Screen, model: CombatModel) -> None:
        self.render_cards(screen, model.deck_manager.hand, model)
        self.render_discard_pile(screen, model)
        self.render_draw_pile(screen, model)

    @staticmethod
    def render_cards(screen: Screen, cards: List[Card], model: CombatModel) -> None:
        n_cards = len(cards)
        assert n_cards < CardArtist.MAX_HAND_SIZE, \
            'handsize {} greater than max {}'.format(n_cards, CardArtist.MAX_HAND_SIZE)
        for i in range(n_cards):
            x, y = card_position(i, n_cards)

            rect = Rect(x, y, CARD_WIDTH, CARD_HEIGHT)

            screen.render_rect(rect, WHITE, 0)
            screen.render_text(cards[i].name, CardArtist.TITLE_FONT, x + 3, y - 3, DARK_GRAY)
            screen.render_text(cards[i].text, CardArtist.BODY_FONT, x + 3, y + 2 * CARD_HEIGHT / 3,
                               DARK_GRAY)
            screen.render_sprite(cards[i].sprite, x + 20, y + 20, CardArtist.SPRITE_SIZE)

            if model.deck_manager.is_selected(i):
                screen.render_rect(model.deck_manager.card_rects[i], RED, 2)

    @staticmethod
    def render_discard_pile(screen: Screen, model: CombatModel) -> None:
        n_discard = len(model.deck_manager.discard)
        discard_x = SCREEN_SIZE[0] - CARD_WIDTH - 50
        discard_y = SCREEN_SIZE[1] - CARD_HEIGHT - 250
        for i in range(n_discard):
            rect = Rect(discard_x + i * 5, discard_y + i * 5, CARD_WIDTH, CARD_HEIGHT)
            screen.render_rect(rect, WHITE, width=0)
            screen.render_rect(rect, DARK_GRAY, width=2)

    @staticmethod
    def render_draw_pile(screen: Screen, model: CombatModel) -> None:
        n_draw = len(model.deck_manager.draw_pile)
        draw_x = 10
        draw_y = SCREEN_SIZE[1] - CARD_HEIGHT - 250
        for i in range(n_draw):
            rect = Rect(draw_x + i * 5, draw_y + i * 5, CARD_WIDTH, CARD_HEIGHT)
            screen.render_rect(rect, WHITE, width=0)
            screen.render_rect(rect, DARK_GRAY, width=2)

from typing import List
from typing import Tuple
import logging
from artists.artist import Artist
from cards.card import Card
from data.colors import WHITE
from data.colors import DARK_GRAY
from data.constants import SCREEN_SIZE
from models.combat_model import CombatModel
from views.pygame_screen import Screen
from pygame.rect import Rect


class CardArtist(Artist):
    CARD_WIDTH = 200
    CARD_HEIGHT = 300
    CARD_FROM_BOTTOM = 250
    CARD_SPACE = 25
    MAX_HAND_SIZE = 7
    TITLE_FONT = 30
    BODY_FONT = 20
    SPRITE_SIZE = (140, 140)

    def render(self, screen: Screen, model: CombatModel) -> None:
        self.render_cards(screen, model.character.cards())

    @staticmethod
    def render_cards(screen: Screen, cards: List[Card]) -> None:
        n_cards = len(cards)
        assert n_cards < CardArtist.MAX_HAND_SIZE, \
            'handsize {} greater than max {}'.format(n_cards, CardArtist.MAX_HAND_SIZE)
        for i in range(n_cards):
            x, y = CardArtist.card_xy(i, n_cards)
            logging.info('card {} @ ({}, {})'.format(i, x, y))
            rect = Rect(x, y, CardArtist.CARD_WIDTH, CardArtist.CARD_HEIGHT)

            screen.render_rect(rect, WHITE, 0)
            screen.render_text(cards[i].name, CardArtist.TITLE_FONT, x + 3, y - 3, DARK_GRAY)
            screen.render_text(cards[i].text, CardArtist.BODY_FONT, x + 3, y + 2 * CardArtist.CARD_HEIGHT / 3,
                               DARK_GRAY)
            screen.render_sprite(cards[i].sprite, x+20, y+20, CardArtist.SPRITE_SIZE)

    @staticmethod
    def card_xy(index: int, hand_size: int) -> Tuple[int]:
        y = SCREEN_SIZE[1] - CardArtist.CARD_FROM_BOTTOM - CardArtist.CARD_HEIGHT
        screen_width = SCREEN_SIZE[0]
        hand_width = hand_size * CardArtist.CARD_WIDTH + (hand_size - 1) * CardArtist.CARD_SPACE
        first_card_x = (screen_width - hand_width) / 2
        x = first_card_x + (CardArtist.CARD_WIDTH + CardArtist.CARD_SPACE) * index
        return (x, y)

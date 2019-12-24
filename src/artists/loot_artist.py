from pygame.rect import Rect

from artists.artist import Artist
from cards.card_position import loot_position
from data.constants import CARD_HEIGHT, CARD_WIDTH
from models.loot_model import LootModel
from views.pygame_screen import Screen


class LootArtist(Artist):
    MAX_HAND_SIZE = 7

    def render(self, screen: Screen, model: LootModel) -> None:
        cards = model.loot_manager.cards
        n_cards = len(cards)
        for i in range(n_cards):
            x, y = loot_position(i, n_cards)
            rect = Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
            screen.render_card(cards[i].name, cards[i].text, rect,
                               cards[i].sprite, model.loot_manager.is_selected(i))

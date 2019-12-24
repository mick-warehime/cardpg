from actors.actor import Actor
from cards.card import Card
from cards.card_manager import CardManager
from cards.loot_manager import LootManager
from models.model import Model


class LootModel(Model):

    def __init__(self, looted_actor: Actor) -> None:
        self.loot_manager = LootManager(looted_actor.cards())

    def selected_card(self) -> Card:
        index = self.loot_manager.selected_index
        if index != CardManager.NONE_SELECTED:
            return self.loot_manager.cards[index]
        return None

from actors.characters.warrior import Warrior
from actors.monsters.skeleton import Skeleton
from cards.deck_manager import DeckManager
from items.club import Club
from items.mace import Mace
from models.model import Model


class CombatModel(Model):

    def __init__(self) -> None:
        self.character = Warrior.new()
        self.character.add_item(Mace())
        self.character.add_item(Club())

        self.deck_manager = DeckManager(self.character.cards())

        self.skeleton = Skeleton.new()
        self.skeleton.add_item(Club())

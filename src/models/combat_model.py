from actors.characters.warrior import Warrior
from actors.monsters.skeleton import Skeleton
from items.club import Club
from items.mace import Mace
from models.model import Model


class CombatModel(Model):

    def __init__(self) -> None:
        self.character = Warrior.new()
        self.character.add_item(Mace())

        self.skeleton = Skeleton.new()
        self.skeleton.add_item(Club())

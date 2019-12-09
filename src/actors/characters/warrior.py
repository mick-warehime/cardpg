from actors.characters.character import Character
from actors.characters.character_type import CharacterType


class Warrior(Character):
    NAME = 'co-nan'
    MAX_HP = 45

    def __init__(self, name: str, max_hp: int) -> None:
        super().__init__(name, max_hp, CharacterType.WARRIOR)

    @staticmethod
    def new() -> Character:
        return Warrior(Warrior.NAME, Warrior.MAX_HP)

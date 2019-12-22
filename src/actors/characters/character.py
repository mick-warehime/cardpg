from typing import Tuple

from actors.actor import Actor, ActorType
from actors.characters.character_type import CharacterType


class Character(Actor):

    def __init__(self,
                 name: str,
                 max_hp: int,
                 character_type: CharacterType,
                 sprite: Tuple[int, int]) -> None:
        super().__init__(name, max_hp, ActorType.CHARACTER, sprite)
        self._character_type = character_type

    @property
    def character_type(self) -> CharacterType:
        return self._character_type

    @staticmethod
    def new() -> 'Character':
        pass

from actors.actor import Actor, ActorType
from actors.monsters.monster_type import MonsterType


class Monster(Actor):

    def __init__(self, name: str, max_hp: int, monster_type: MonsterType) -> None:
        super().__init__(name, max_hp, ActorType.MONSTER)
        self._monster_type = monster_type

    @property
    def monster_type(self) -> MonsterType:
        return self._monster_type

    @staticmethod
    def new() -> 'Monster':
        pass

    # Add starting item distribution (probability distribution over items)

from actors.monsters.monster import Monster
from actors.monsters.monster_type import MonsterType


class Skeleton(Monster):
    NAME = 'Skellie'
    MAX_HP = 15
    SPRITE = (5, 1)

    def __init__(self, name: str, max_hp: int) -> None:
        super().__init__(name, max_hp, MonsterType.SKELETON, Skeleton.SPRITE)

    @staticmethod
    def new() -> Monster:
        return Skeleton(Skeleton.NAME, Skeleton.MAX_HP)

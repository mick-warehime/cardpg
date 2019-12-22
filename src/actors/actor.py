import abc
from typing import List, Tuple

from actors.actor_type import ActorType


class Actor(object):

    def __init__(self,
                 name: str,
                 max_hp: int,
                 actor_type: ActorType,
                 sprite: Tuple[int, int]) -> None:
        self._name = name
        self._actor_type = actor_type
        self._hp = max_hp
        self._max_hp = max_hp
        self._items: List['Item'] = []
        self._sprite = sprite

    @property
    def name(self) -> str:
        return self._name

    @property
    def actor_type(self) -> ActorType:
        return self._actor_type

    @property
    def hp(self) -> int:
        return self._hp

    @hp.setter
    def hp(self, hp: int) -> None:
        self._hp = hp

    @property
    def max_hp(self) -> int:
        return self._max_hp

    def add_item(self, item: 'Item') -> None:
        self._items.append(item)

    def cards(self) -> List['Card']:
        all_cards = []
        for item in self._items:
            all_cards += item.grants_cards()
        return all_cards

    @abc.abstractmethod
    def new(self) -> 'Actor':
        pass

    def __str__(self) -> str:
        return self.name

    @property
    def sprite(self) -> Tuple[int, int]:
        return self._sprite

    # Add Skill (effectively upgrades) cards may require skills or benefit from extra skills

from typing import List
from typing import Tuple

from actions.action import Action
from actors.actor import Actor
from events.event_manager import EventManager
from events.play_card_event import PlayCardEvent


class Card(object):

    def __init__(self, name: str, sprite: Tuple[int, int], text: str, actions: List[Action]) -> None:
        self.name = name
        self.sprite = sprite
        self.text = text
        self.actions = actions

    def play(self, actor: Actor, target: Actor) -> None:
        EventManager.post(PlayCardEvent(self))
        for action in self.actions:
            action.act(actor, target)

    def __str__(self) -> str:
        return self.name

    # add randomization of base card action potential (mace 8 + 2d2), (kite shield 4+1d1)
    # add skill impact

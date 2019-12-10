from typing import List

from actions.action import Action
from actors.actor import Actor


class Card(object):

    def __init__(self, actions: List[Action]) -> None:
        self.actions = actions

    def play(self, actor: Actor, target: Actor) -> None:
        for action in self.actions:
            action.act(actor, target)

    # add randomization of base card action potential (mace 8 + 2d2), (kite shield 4+1d1)
    # add skill impact

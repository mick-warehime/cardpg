import abc

from actions.action_type import ActionType
from actors.actor import Actor


class Action(object):

    def __init__(self, action_type: ActionType) -> None:
        self.action_type = action_type

    @abc.abstractmethod
    def act(self, actor: Actor, target: Actor) -> None:
        pass

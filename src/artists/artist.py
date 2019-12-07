import abc

from models.model import Model
from views.pygame_screen import Screen


class Artist(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def render(self, screen: Screen, model: Model) -> None:
        """Generic function to render content to a screen."""

from artists.card_artist import CardArtist
from artists.combat_artist import CombatArtist
from views.view import View


class CombatView(View):

    def __init__(self) -> None:
        View.__init__(self, [CombatArtist(), CardArtist()])

from views.view import View
from artists.combat_artist import CombatArtist


class CombatView(View):

    def __init__(self) -> None:
        View.__init__(self, [CombatArtist()])

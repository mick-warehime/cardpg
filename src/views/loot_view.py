from artists.loot_artist import LootArtist
from views.view import View


class LootView(View):

    def __init__(self) -> None:
        View.__init__(self, [LootArtist()])

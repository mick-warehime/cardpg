from views.view import View
from artists.settings_artist import SettingsArtist


class SettingsView(View):

    def __init__(self) -> None:
        View.__init__(self, [SettingsArtist()])

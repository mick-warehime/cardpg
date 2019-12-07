from artists.settings_artist import SettingsArtist
from views.view import View


class SettingsView(View):

    def __init__(self) -> None:
        View.__init__(self, [SettingsArtist()])

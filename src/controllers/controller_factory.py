from controllers.controller import Controller
from controllers.settings_controller import SettingsController
from controllers.combat_controller import CombatController
from models.settings_model import SettingsModel
from models.combat_model import CombatModel
from views.settings_view import SettingsView
from views.combat_view import CombatView


def build_controller(next_screen: str) -> Controller:
    if next_screen == 'settings':
        return SettingsController(SettingsModel(), SettingsView())
    elif next_screen == 'combat':
        return CombatController(CombatModel(), CombatView())
    raise AssertionError('no controller defined for next_screen:{}'.format(next_screen))

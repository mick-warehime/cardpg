from controllers.combat_controller import CombatController
from controllers.controller import Controller
from controllers.settings_controller import SettingsController
from models.combat_model import CombatModel
from models.settings_model import SettingsModel
from views.combat_view import CombatView
from views.settings_view import SettingsView


def build_controller(next_screen: str) -> Controller:
    if next_screen == 'settings':
        return SettingsController(SettingsModel(), SettingsView())
    elif next_screen == 'combat':
        return CombatController(CombatModel(), CombatView())
    raise AssertionError('no controller defined for next_screen:{}'.format(next_screen))

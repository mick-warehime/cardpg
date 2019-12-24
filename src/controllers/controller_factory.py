from controllers.combat_controller import CombatController
from controllers.controller import Controller
from controllers.loot_controller import LootController
from controllers.settings_controller import SettingsController
from events.event import Event
from models.combat_model import CombatModel
from models.loot_model import LootModel
from models.settings_model import SettingsModel
from views.combat_view import CombatView
from views.loot_view import LootView
from views.settings_view import SettingsView


def build_controller(event: Event) -> Controller:
    if event.next_screen == 'settings':
        return SettingsController(SettingsModel(), SettingsView())
    elif event.next_screen == 'combat':
        return CombatController(CombatModel(), CombatView())
    elif event.next_screen == 'loot':
        return LootController(LootModel(event.actor), LootView())
    raise AssertionError('no controller defined for next_screen:{}'.format(event.next_screen))

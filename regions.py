from typing import List, Set, Dict, Tuple, Optional, Callable, NamedTuple
from BaseClasses import Multiworld, Region, Entrance, Location, RegionType
from .locations import LocationData
from ..generic.Rules import add_rule, set_rule, forbid_item
from Items import get_item_type
from .options import get_option_value
# import Monster Sanctuary Yaml stuff
import random

def create_regions(world: MulitWorld, player: int, locations: Tuple[LocationData, ...], location_cache: List[Location]):
    locations_per_region = get_locations_per_region(locations)

    regions = [
        create_region(world, player, locations_per_region, location_cache, "Menu"),
        create_region(world, player, locations_per_region, location_cache, "Keepers"),
        create_region(world, player, locations_per_region, location_cache, "Mountain Path"),
        create_region(world, player, locations_per_region, location_cache, "Blue Caves"),
        create_region(world, player, locations_per_region, location_cache, "Stronghold"),
        create_region(world, player, locations_per_region, location_cache, "Snowy Peaks"),
        create_region(world, player, locations_per_region, location_cache, "Sun Palace"),
        create_region(world, player, locations_per_region, location_cache, "Ancient Woods"),
        create_region(world, player, locations_per_region, location_cache, "Magma Chamber"),
        create_region(world, player, locations_per_region, location_cache, "Horizon Beach"),
        create_region(world, player, locations_per_region, location_cache, "Workshop"),
        create_region(world, player, locations_per_region, location_cache, "Blob Burg"),
        create_region(world, player, locations_per_region, location_cache, "Underworld"),
        create_region(world, player, locations_per_region, location_cache, "Abandoned Tower"),
        create_region(world, player, locations_per_region, location_cache, "Eternity's End"),
        create_region(world, player, locations_per_region, location_cache, "Forgotten World")
    ]

connect(world, player, names, 'Menu', 'Mountain Path')
connect(world, player, names, 'Mountain Path', 'Keepers', lambda state: state._monsanct_done_tutorial(world, player))
connect(world, player, names, 'Mountain Path', 'Blue Caves')
connect(world, player, names, 'Keepers', 'Blue Caves', lambda state: state._monsanct_done_tutorial(world, player))
connect(world, player, names, 'Mountain Path', 'Snowy Peaks', lambda state: state._monsanct_has_fly(world, player))
connect(world, player, names, 'Blue Caves', 'Mountain Path', lambda state: state._monsanct_has_doublejump(world, player) and state:_monsanct_BlueCaveLever(world, player))
connect(world, player, names, 'Blue Caves', 'Sun Palace', lambda state: state._monsanct_has_earth(world, player) and state._monsanct_has_lightning(world, player))
connect(world, player, names, 'Blue Caves', 'Stronghold', lambda state: state._monsanct_StrongholdLever(world, player))
connect(world, player, names, 'Blue Caves', 'Underworld', lambda state: state._monsanct_has_5tokens(world, player))
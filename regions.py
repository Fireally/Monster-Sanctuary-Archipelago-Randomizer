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
        create_region(world, player, locations_per_region, location_cache, "Eternity End"),
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

connect(world, player, names, 'Stronghold', 'Keepers', lambda state: state._monsanct_is_novice(world, player))
connect(world, player, names, 'Stronghold', 'Workshop', lambda state: state._monsanct_has_superfly(world, player))
connect(world, player, names, 'Stronghold', 'Ancient Woods')
connect(world, player, names, 'Stronghold', 'Ancient Woods')

connect(world, player, names, 'Snowy Peaks', 'Sun Palace', lambda state: state._monsanct_has_thermals(world, player))

connect(world, player, names, 'Ancient Woods', 'Stronghold')
connect(world, player, names, 'Ancient Woods', 'Horizon Beach', lambda state: state._monsanct_2WoodsKeys)

connect(world, player, names, 'Magma Chamber', 'Stronghold', lambda state: state._monsanct_has_mount(world, player))
connect(world, player, names, 'Magma Chamber', 'Blob Burg', lambda state: state._monsanct_has_blobstatues(world, player))
connect(world, player, names, 'Magma Chamber', 'Ancient Woods', lambda state: state._monsanct_MagmaLever(world, player))
connect(world, player, names, 'Magma Chamber', 'Horizon Beach', lambda state: state._monsanct_killed_elderjel(world, player))
connect(world, player, names, 'Magma Chamber', 'Forgotten World', lambda state: state._monsanct_has_bigrock(world, player))

connect(world, player, names, 'Horizon Beach', 'Forgotten World', lambda state: state._monsanct_has_secret(world, player))
connect(world, player, names, 'Horizon Beach', 'Forgotten World', lambda state: state._monsanct_has_bigrock(world, player))

connect(world, player, names, 'Workshop', 'Abandoned Tower', lambda state: state._monsanct_has_keyofpower(world, player))

connect(world, player, names, 'Underworld', 'Sun Palace', lambda state: state._monsanct_UnderLever(world, player))

connect(world, player, names, 'Eternity End', 'Keepers', lambda state: state._monsanct_is_master(world, player))


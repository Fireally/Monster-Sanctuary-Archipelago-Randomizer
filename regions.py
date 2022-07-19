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

def set_rules(self)
    set_rule(self.world.get_entrance("Keepers", self.player),
             lambda state: state.has("Buran Tutorial", self.player))
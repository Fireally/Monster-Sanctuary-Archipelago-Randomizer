from typing import List, Tuple, Optional, Callable, NamedTuple
from BaseClasses import MultiWorld
from .options import is_option_enabled

EventId: Optional[int] = None

class MonsterSanctLocation(Location):
    game: str = "monster-sanctuary"

class LocationData(NamedTuple):
    region: str
    name: str
    code: Optional[int]
    rule: Callable = lambda state: True

#Offset integer jic.
MonSanctIdOffset = 0


def get_locations(world: Optional[MultiWorld], player: Optional[int]) -> Tuple[LocationData, ...]:
    location_table: List[LocationData] = [
        LocationData('Keepers', 'Mother Gift', 0 + MonSanctIdOffset),
        LocationData('Keepers', 'Father Gift', 1 + MonSanctIdOffset),
        LocationData('Keepers', 'Father Seeker', 2 + MonSanctIdOffset, lambda state: state._monsanct_is_seeker(world,
            player))
    ]
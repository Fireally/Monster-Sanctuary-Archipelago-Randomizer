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
        #Keeper's Stronghold (10)locations.
        LocationData('Keepers', 'Mother Gift', 0 + MonSanctIdOffset),
        LocationData('Keepers', 'Father Gift', 1 + MonSanctIdOffset),
        LocationData('Keepers', 'Father Seeker', 2 + MonSanctIdOffset, lambda state: state._monsanct_is_seeker(world,
            player))
        LocationData('Keepers', 'Father Ranger', 3 + MonSanctIdOffset, lambda state: state._monsanct_is_ranger(world, player))
        LocationData('Keepers', 'Father Champion', 4 + MonSanctIdOffset, lambda state: state._monsanct_is_champion(world, player))
        LocationData('Keepers', 'Father Master', 5 + MonSanctIdOffset, lambda state: state._monsanct_is_master(world, player))
        LocationData('Keepers', 'Room 1', 6+MonSanctIdOffset),
        LocationData('Keepers', 'Room 2', 7+MonSanctIdOffset),
        LocationData('Keepers', 'Room 3-1', 8 + MonSanctIdOffset),
        LocationData('Keepers', 'Room 3-2', 9 + MonSanctIdOffset),

        #Mountain Path (34) locations
        LocationData('Mountain', 'Room 1', 10 + MonSanctIdOffset),
        LocationData('Mountain', 'Room 2', 11 + MonSanctIdOffset, lambda state: state._monsanct_has_DW(world, player)),
        LocationData('Mountain', 'Room 3', 12 + MonSanctIdOffset),
        LocationData('Mountain', 'Room 4', 13 + MonSanctIdOffset, lambda state: state._monsanct_has_fly(world,player)
            or state: state._monsanct_has_doublejump(world,player)),

        #Blue Caves (39) locations

        #Stronghold Dungeon (32) locations

        #Snowy Peaks (50) locations

        #Sun Palace (31) locations

        #Ancient Woods (42) locations

        #Magma Chamber (49) locations

        #Horizon Beach (45) locations

        #Mystical Workshop (35) locations

        #Blob Burg (19) locations

        #Underworld (29) locations

        #Abandoned Tower (27) locations

        #Eternity's End (2) locations

        #Forgotten World (57) locations

        #Boss Battle (12) locations

    ]
from typingimport Dict
from BaseClasses import MultiWorld
from Options import Choice, Option, DefaultOnToggle

class Goal(Choice):
    """What the objective of this playthrough will be? The Mad One is beat the main story, 5 Sanctuary Tokens is for
    faster games, ending when the Underworld is opened in Blue Caves, Defeat Godzerker is a much longer game, ending
    with the defeat of the penultimate boss of the game, and Blob Berg is the shortest goal, ending with defeating
    the Champion Monster in the Blob Burg"""
    display_name = "Game Objective"
    option_blob = 0
    option_tokens = 1
    option_madone = 2
    option_Godzerker = 3

class SkipTutorial(DefaultOnToggle):
    """Skip the tutorial, starting at Keeper Aspirant. Mountain Path, Blue Cave, and the Stronghold will be available
    immediately. This will automatically count the Steam Golem as defeated"""
    display_name = "Skipped Tutorial"

class ColoredChests(DefaultOnToggle):
    """When turned on, the chests in the world will have different colors depending on the usefulness of the item
    inside. Filler is brown, Useful is white, progression is green, and goals are purple."""
    display_name = "Colored Chests"

class RandomizedExplorationAbilities(DefaultOnToggle):
    """When turned on, all monsters have a random exploration ability assigned to them and adds them to progression
    logic as normal."""
    display_name = "Random Exploration Abilities"

class RandomizedStarters(DefaultOnToggle):
    """Your choice of starting monster at the start of the game is randomized, rather than the usual Spectral
    Familiars."""
    display_name = "Randomized Starters"

class IsBrave(DefaultOnToggle):
    """This activates Brave-Mode chests and logic into the run."""
    display_name = "Use Bravemode?"

class RandomizeChampions(DefaultOnToggle):
    """Randomize all the Champion Monsters in the game."""
    display_name = "Randomize Champions?"

class RandomizeKeepers(Choice):
    """Randomize the teams Keepers have in the game. It can be turned off, logical (characters will shift previously
    owned monsters, Chymes will have the Spectrals, etc), or completely random"""
    display_name = "Keeper Randomization"
    option_vanilla = 0
    option_logical = 1
    option_allrandom = 2


def get_option_value(world: MultiWorld, player: int, name: str) -> int:
    option = getattr(world, name, None)

    if option == None:
        return 0

    return int(option[player].value)
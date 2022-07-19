from BaseClasses import Item, ItemClassification
import typing

class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    type: typing.Optional[str]
    number: typing.Optional[int]
    classification: ItemClassification = ItemClassification.useful
    quantity: int = 1

def get_full_item_list(self):
    return item_table

MonSanctItemIdOffset = 0

item_table = {
    #Combat Consumable Items
    "3x Potion": ItemData(1 + MonSanctItemIdOffset, "Combat", 0, classification=ItemClassification.filler),
    "3x Phoenix Tear": ItemData(25+ MonSanctItemIdOffset, "Combat", 1, classification=ItemClassification.filler),

    #Accesory Items
    "Brooch": ItemData(0 + MonSanctItemIdOffset, "Accessory", 0, classification=ItemClassification.useful),
    "Hide+1": ItemData(9 + MonSanctItemIdOffset, "Accessory", 1, classification=ItemClassification.filler),
    "Cape": ItemData(13 + MonSanctItemIdOffset, "Accessory", 2, classification=ItemClassification.filler),
    "Vital Ring": ItemData(15 + MonSanctItemIdOffset, "Accessory", 3, classification=ItemClassification.filler),
    "Hide": ItemData(17+ MonSanctItemIdOffset, "Accessory", 4, classification=ItemClassification.filler),
    "Bracelet": ItemData(18 + MonSanctItemIdOffset, "Accessory", 5, classification=ItemClassification.filler),
    "Gauntlet": ItemData(19 + MonSanctItemIdOffset, "Accessory", 6, classification=ItemClassification.filler),
    "Diadem": ItemData(21 + MonSanctItemIdOffset, "Accessory", 7, classification=ItemClassification.filler),
    "Impact Ring": ItemData(24 + MonSanctItemIdOffset, "Accessory", 8, classification=ItemClassification.filler),
    "Bandana": ItemData(28 + MonSanctItemIdOffset, "Accessory", 9, classification=ItemClassification.filler),
    "Crit Ring": ItemData(30 + MonSanctItemIdOffset, "Accessory", 10, classification=ItemClassification.filler),

    #Weapon Items
    "Staff": ItemData(10 + MonSanctItemIdOffset, "Weapon", 0, classification=ItemClassification.filler),
    "Cestus": ItemData(14+ MonSanctItemIdOffset, "Weapon", 1, classification=ItemClassification.filler),
    "Kunai": ItemData(16+ MonSanctItemIdOffset, "Weapon", 2, classification=ItemClassification.filler),
    "Orb": ItemData(22 + MonSanctItemIdOffset, "Weapon", 3, classification=ItemClassification.filler),
    "Morning Star": ItemData(23 + MonSanctItemIdOffset, "Weapon", 4, classification=ItemClassification.filler),

    #Money Chests
    "150G": ItemData(27+ MonSanctItemIdOffset, "Money", 0, classification=ItemClassification.filler),

    #Consumable Items
    "Reward Box 1": ItemData(2 +MonSanctItemIdOffset, "Consumable", 0, classification=ItemClassification.filler, quantity=3),
    "Reward Box 2": ItemData(3 +MonSanctItemIdOffset, "Consumable", 1, classification=ItemClassification.filler, quantity=5),
    "Reward Box 3": ItemData(4 +MonSanctItemIdOffset, "Consumable", 2, classification=ItemClassification.useful, quantity=2),
    "2x Reward Box 3": ItemData(5 +MonSanctItemIdOffset, "Consumable", 3, classification=ItemClassification.useful, quantity=3),
    "Reward Box 4": ItemData(6+MonSanctItemIdOffset, "Consumable", 4, classification=ItemClassification.useful),
    "2X Reward Box 4": ItemData(7 + MonSanctItemIdOffset, "Consumable", 5, classification=ItemClassification.useful, quantity=3),
    "3X Reward Box 4": ItemData(8 + MonSanctItemIdOffset, "Consumable", 6, classification=ItemClassification.useful),
    "Skill Resetter": ItemData(11+MonSanctItemIdOffset, "Consumable", 7, classification=ItemClassification.filler, quantity=6),
    "3X Skill Resetter": ItemData(12 + MonSanctItemIdOffset, "Consumable", 8, classification=ItemClassification.filler),
    "3x Smokebomb": ItemData(31 + MonSanctItemIdOffset, "Consumable", 9, classification=ItemClassification.filler, quantity=2),

    #Crafting Items
    "2x Copper": ItemData(20+MonSanctItemIdOffset, "Crafting", 0, classification=ItemClassification.filler),
    "Red Gem": ItemData(26 + MonSanctItemIdOffset, "Crafting", 1, classification=ItemClassification.filler, quantity=7),

    #Food Items
    "Walnut": ItemData(29 + MonSanctItemIdOffset, "Food", 0, classification=ItemClassification.filler),


}

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

#activate comment if we need an item offset monster-sanctuary-ItemIdOffset = 2000

item_table = {
    "Brooch": ItemData(0), "Accessory", 0, classification=ItemClassification.useful
    "3x Potion": ItemData(1), "Combat", 1, classification=ItemClassification.filler
    "Reward Box 1": ItemData(2), "Consumable", 2, classification=ItemClassification.filler
        #There's like 20 of these things throughout the game, surely there's a way to just put in 20 into the list and call it a day?
}

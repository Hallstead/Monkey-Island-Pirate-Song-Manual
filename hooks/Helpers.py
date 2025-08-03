from typing import Optional, TYPE_CHECKING
from BaseClasses import MultiWorld, Item, Location
from .. import Helpers

if TYPE_CHECKING:
    from ..Items import ManualItem
    from ..Locations import ManualLocation

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the category, False to disable it, or None to use the default behavior
def before_is_category_enabled(multiworld: MultiWorld, player: int, category_name: str) -> Optional[bool]:
    if category_name == "Guybrush":
        if Helpers.get_option_value(multiworld, player, "Part_to_Sing") in [0, 1, 5]:
            return True
        return False
    if category_name == "Bill":
        if Helpers.get_option_value(multiworld, player, "Part_to_Sing") in [2, 5]:
            return True
        return False
    if category_name == "Haggis":
        if Helpers.get_option_value(multiworld, player, "Part_to_Sing") in [3, 5]:
            return True
        return False
    if category_name == "Edward":
        if Helpers.get_option_value(multiworld, player, "Part_to_Sing") in [4, 5]:
            return True
        return False
    if category_name == "Not Verse":
        if Helpers.get_option_value(multiworld, player, "Part_to_Sing") in [0]:
            return False
        return True
    if category_name == "All":
        if Helpers.get_option_value(multiworld, player, "Part_to_Sing") in [2, 3, 4, 5]:
            return True
        return False
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the item, False to disable it, or None to use the default behavior
def before_is_item_enabled(multiworld: MultiWorld, player: int, item: "ManualItem") -> Optional[bool]:
    return None

# Use this if you want to override the default behavior of is_option_enabled
# Return True to enable the location, False to disable it, or None to use the default behavior
def before_is_location_enabled(multiworld: MultiWorld, player: int, location: "ManualLocation") -> Optional[bool]:
    return None

# items.py
from enum import Enum
from typing import TYPE_CHECKING

# To avoid Circular Import and Ensure character is available
if TYPE_CHECKING:
    from characters import Character


# Creating Custom Type of my Items
class ItemType(Enum):
    BUFF = "buff"
    WEAPON = "weapon"


# Base Class
class Item:
    def __init__(self, name: str, type: ItemType) -> None:
        self.__name: str = name
        self.__type: ItemType = type

    # Getter for item name
    def get_name(self) -> str:
        return self.__name

    # Getter for Tpye
    def get_type(self) -> ItemType:
        return self.__type

    # Returns a summary of the item
    def __str__(self) -> str:
        return f"{self.__name} - {self.__type.value}"


# Sub Class: Type - buff, Healing Potion
class HealingPotion(Item):
    def __init__(
        self,
        name: str,
        increased_health_by: float
    ) -> None:
        super().__init__(name, ItemType.BUFF)
        self.__stat_affected: str = "healing"
        self.__increased_health_by: float = increased_health_by

    # How much this potion heals.
    def get_increased_health_by(self) -> float:
        return self.__increased_health_by

    # Which stat this potion affects.
    def get_stat_affected(self) -> str:
        return self.__stat_affected

    # Apply the healing effect to the target character
    def use(self, target: "Character") -> None:
        target.update_healing("add", self.__increased_health_by)

    def __str__(self) -> str:
        return (
            f"{self.__name} - Buff Potion "
            f"(+{self.__increased_health_by} to {self.__stat_affected})"
        )


# Sub Class: Type - buff, Strength buff
class StrengthBuff(Item):
    def __init__(
        self,
        name: str,
        increased_strength_by: float
    ) -> None:
        super().__init__(name, ItemType.BUFF)
        self.__stat_affected: str = "strength"
        self.__increased_strength_by: float = increased_strength_by

    # How much this potion heals.
    def get_increased_strength_by(self) -> float:
        return self.__increased_strength_by

    # Which stat this potion affects.
    def get_stat_affected(self) -> str:
        return self.__stat_affected

    # Apply the healing effect to the target character
    def use(self, target: "Character") -> None:
        target.update_strength("add", self.__increased_strength_by)

    def __str__(self) -> str:
        return (
            f"{self.__name} - Buff Potion "
            f"(+{self.__increased_strength_by} to {self.__stat_affected})"
        )


# Sub Class: type - weapon
class Sniper(Item):
    def __init__(
        self, name: str,
        range_multiplier: float,
    ) -> None:
        super().__init__(name, ItemType.WEAPON)
        self.__base_damage: float = 145.7
        self.__range_multiplier: float = range_multiplier
        # Total Damage Scales with range
        self.__damage_inflicted: float = self.__base_damage * range_multiplier

    # Sniper Base Damage
    def get_base_damage(self) -> float:
        return self.__base_damage

    # Total Damage caused by sniper
    def get_damage_inflicted(self) -> float:
        return self.__damage_inflicted

    # Range Of Shot
    def get_range_multiplier(self) -> float:
        return self.__range_multiplier

    # Apply Damage to the enemy and update character damage inflictd
    def use(self, target: "Character") -> None:
        target.update_damage_inflicted(self.__damage_inflicted)

    def __str__(self) -> str:
        return (
            f"{self.__name} - Sniper Rifle "
            f"(Damage: {self.__damage_inflicted:.1f}, "
            f"Range ×{self.__range_multiplier})"
        )

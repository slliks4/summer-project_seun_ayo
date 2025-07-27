# characters.py

import random
from typing import List

from items import Item


# Base Class
class Character:
    # Constructor
    def __init__(
        self,
        name: str,
        # Character Stats (These are gotten from the sub characters)
        strength: float,
        agility: float,
        intelligence: float,
        speed: float,
        healing: float,
    ) -> None:
        self.__name: str = name
        # Random age between 100 - 400
        self.__age: int = random.randint(100, 400)
        # Bag Pack or Inventory
        self.__inventory: List[Item] = []

        # Core stats initialized to zero
        self.__strength: float = strength
        self.__agility: float = agility
        self.__intelligence: float = intelligence
        self.__speed: float = speed
        self.__healing: float = healing

        # Damage Inflicted to enemy
        self.__total_damage_inflicted = 0

    # Getters for accessing private fields when needed
    def get_name(self) -> str:
        return self.__name

    # Getter for accessing Inventory(Items List)
    def get_inventory(self) -> List[Item]:
        return self.__inventory

    # Getter for Total Damage inflicted by Character to enemy
    def get_total_damage_inflicted(self) -> float:
        return self.__total_damage_inflicted

    # Method: Add item to inventory
    def add_item(self, item: Item) -> None:
        self.__inventory.append(item)

    # Method: Remove item to inventory
    def remove_item(self, item: Item) -> None:
        self.__inventory.remove(item)

    # Method: updates Damage inflicted
    def update_damage_inflicted(self, amount: float) -> None:
        self.__total_damage_inflicted += amount

    # PlaceHolder: Overridden by subclass
    def use_special_ability(self, other: "Character") -> None:
        raise NotImplementedError(
            "Each character must define their special ability."
        )

    def update_strength(self, operator: str, amount: float) -> bool:
        # Increase Character Strenght
        if operator == 'add':
            self.__strength += amount

        # Reduce Character Strenght
        if operator == 'subtract':
            # Logic for minimum and maximum strenght
            if self.__strength == 0:
                return False
            self.__strength -= amount

        return True

    def update_agility(self, operator: str, amount: float) -> bool:
        # Increase Character Strenght
        if operator == 'add':
            self.__agility += amount

        # Reduce Character Strenght
        if operator == 'subtract':
            # Logic for minimum and maximum strenght
            if self.__agility == 0:
                return False
            self.__agility -= amount

        return True

    def update_intelligence(self, operator: str, amount: float) -> bool:
        # Increase Character Strenght
        if operator == 'add':
            self.__intelligence += amount

        # Reduce Character Strenght
        if operator == 'subtract':
            # Logic for minimum and maximum strenght
            if self.__intelligence == 0:
                return False
            self.__intelligence -= amount

        return True

    def update_speed(self, operator: str, amount: float) -> bool:
        # Increase Character Strenght
        if operator == 'add':
            self.__speed += amount

        # Reduce Character Strenght
        if operator == 'subtract':
            # Logic for minimum and maximum strenght
            if self.__speed == 0:
                return False
            self.__speed -= amount

        return True

    def update_healing(self, operator: str, amount: float) -> bool:
        # Increase Character Strenght
        if operator == 'add':
            self.__healing += amount

        # Reduce Character Strenght
        if operator == 'subtract':
            # Logic for minimum and maximum strenght
            if self.__healing == 0:
                return False
            self.__healing -= amount

        return True

    # Readable summary of character
    def __str__(self) -> str:
        stats = (
            f"Strength: {self.__strength}\n"
            f"Agility: {self.__agility}\n"
            f"Intelligence: {self.__intelligence}\n"
            f"Speed: {self.__speed}\n"
            f"Healing: {self.__healing}"
        )

        # List inventory names or show 'Empty'
        if len(self.__inventory) == 0:
            inventory_list = "Empty"
        else:
            inventory_list = ''
            for item in self.__inventory:
                inventory_list += item.get_name() + ", "
            # Remove trailing comma and Space
            inventory_list = inventory_list[:-2]

        return (
            f"Name: Survivor {self.__name}\n"
            f"age: {self.__age}\n"
            f"Damage Inflicted: {self.__total_damage_inflicted}\n"
            f"Inventory: {inventory_list}\n"
            f"Core Stats ------------ \n{stats}\n"
        )


# Hulk man Sub class
class HulkMan(Character):
    def __init__(self, name: str):
        super().__init__(
            name,
            strength=9.2,
            agility=10,
            intelligence=9,
            speed=7,
            healing=6
        )
        # Unique Attribute for HulkMan
        self.__rage: float = 0

    def use_special_ability(self, other: Character) -> None:
        if self.__rage == 10:
            self.__rage = 0
            print(
                f"""
                {self.get_name()} unleashes RAGE SMASH!
                Increasing total strenght and speed
                """
            )

    def __str__(self) -> str:
        return super().__str__() + f"\nRage: {self.__rage}"


# HealerWoman Sub class
class HealerWoman(Character):
    def __init__(self, name: str):
        super().__init__(
            name,
            strength=3,
            agility=7,
            intelligence=10,
            speed=6,
            healing=10
        )
        # Unique Attribute for HulkMan
        self.__healing_power: float = 0

    def use_special_ability(self, other: Character) -> None:
        if self.__healing_power == 10:
            self.__healing_power = 0
            print(
                f"""
                {self.get_name()} unleashes RAGE SMASH!
                Increasing total strenght and speed
                """
            )

    def __str__(self) -> str:
        return super().__str__() + f"\nHealing Power: {self.__healing_power}"

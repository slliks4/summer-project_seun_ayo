# main.py

from characters import Character, HealerWoman, HulkMan
from items import HealingPotion, Sniper, StrengthBuff


# Introduction To the Game
def intro() -> str:
    print("🌍 Welcome to MOAB Games: Mother Of All Battles 🌍\n")
    player_name = input("Enter your name to begin: ")
    print(f"\nWakie Wakie, Survivor {player_name}!")
    print("""
As you know, Earth as we once knew it has fallen.
War. AI takeover. Collapse.
You are a survivor from the Moab Order — Earth’s final resistance.

Your mission:
- Survive the warzone of Earth 2.0
- Rescue clean humans
- Destroy corrupted enemies (AI and Revolutionists)

Your stats, your items, and your choices will determine your role and survival.

Godspeed.
    """)
    return player_name


# Character Selection
def select_character(name: str):
    # Loops Till a User select a Valid option
    while True:
        print("\nChoose your character:")
        print("1. Base Character")
        print("2. Hulk Man")
        print("3. Healer Woman")
        print("0. Quit Game")
        choice = input("Your choice: ")

        # Character 1 - Base Character
        if choice == "1":
            return Character(
                name,
                strength=0,
                agility=0,
                intelligence=0,
                speed=0,
                healing=0
            )

        # Character 2 - HulkMan
        if choice == "2":
            return HulkMan(name)
        # Character 1 - HulkMan
        if choice == "3":
            return HealerWoman(name)
        # Quite Game
        elif choice == "0":
            print("Farewell, warrior.")
            exit()
        # Catch for Invalid Options
        else:
            print("Invalid choice. Try again.")


# Item Selection
def select_item(character):
    # Loops Till a User select a Valid option
    while True:
        print("\nChoose an item to carry:")
        print("1. Healing Potion (+5 Healing)")
        print("2. Strength Buff(+5 Strength)")
        print("3. Sniper Rifle (Damage x1.5)")
        print("0. No Item")
        item = input("Your choice: ")

        # Item 1 - Potion
        if item == "1":
            potion = HealingPotion("Nano Healing", increased_health_by=5)
            character.add_item(potion)
            print("Healing Potion added.")
            break
        # Item 2 - Strength Buff
        if item == "2":
            strength_buff = StrengthBuff(
                "Super Concrete",
                increased_strength_by=5
            )
            character.add_item(strength_buff)
            print("Strength Buff added.")
            break
        # Item 2 - Sniper rifle
        elif item == "3":
            sniper = Sniper("Eagle Sniper", range_multiplier=1.5)
            character.add_item(sniper)
            print("Sniper Rifle added.")
            break
        # No Item Selected
        elif item == "0":
            print("No item selected.")
            break
        # Wrong Input
        else:
            print("Invalid input. Try again.")


# Use Item
def use_item(character):
    # Get the list of Item in Character Inventory
    inventory = character.get_inventory()

    if not inventory:
        print("Inventory is empty.")
        return

    print("\nInventory:")

    # Item Count
    count = 1
    # Loop and list out character items
    for item in inventory:
        print(f"{count}. {item.get_name()}")
        count += 1

    # Throw an error if user enters anything except from an ineger
    try:
        choice = int(input("Use which item? (0 to cancel): "))
    except ValueError:
        print("Invalid input.")
        return

    # This is because python indexing starts from 0 not 1
    index = choice - 1
    # Check if index is in range
    if 0 <= index < len(inventory):
        # Get That particular item from inventory
        item = inventory[index]
        # Checks if The Class has the attribute use
        if hasattr(item, 'use'):
            # Use Item
            item.use(character)
            # Remove Item from inventory
            character.remove_item(item)
            print(f"Used {item.get_name()}.")
        else:
            print("This item cannot be used.")
    elif int(choice) == 0:
        return

    # Throw error if none of the conditions above are satisfied
    else:
        print("Invalid choice.")


# Game Loop
def game_loop():
    # Starts the Intro of the game
    player_name = intro()
    # Character Object
    character = select_character(player_name)
    select_item(character)

    # Loop to Keep the Game going
    while True:
        print("\nWhat would you like to do next?")
        print("1. View Character Summary")
        print("2. Add More Item")
        print("3. Use Item")
        print("4. Use Special Ability")
        print("0. Quit")

        action = input("Select an option: ")

        # Character Summary
        if action == "1":
            print("\n--- Character Summary ---")
            print(character)
        # Add more Item
        elif action == "2":
            select_item(character)
        # Use Item in inventory
        elif action == "3":
            use_item(character)
        # Use Special Ability
        elif action == "4":
            character.use_special_ability(character)

        # End Game
        elif action == "0":
            print("Game ended. See you in the next battle!")
            break
        else:
            print("Invalid input. Try again.")


# --- Start Game ---
if __name__ == "__main__":
    game_loop()

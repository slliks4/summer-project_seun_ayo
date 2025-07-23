from characters import DiamondPlayer
from items import GetHint
import random

# Create player
player = DiamondPlayer("suen", 1, 5)

# Create puzzle bank
puzzles = [
    GetHint(1, "P__hon", "Python", "Popular programming language"),
    GetHint(4, "J__a", "Java", "Coffee or code"),
    GetHint(4, "H__ML", "HTML", "Markup language for websites"),
    GetHint(4, "CS__", "CSS", "Used to style HTML"),
    GetHint(4, "J__aSc__pt", "JavaScript", "Client-side scripting language"),
    GetHint(4, "Al__r__thm", "Algorithm", "Step-by-step procedure"),
    GetHint(4, "D__ta", "Data", "What you process"),
    GetHint(4, "N__tw__rk", "Network", "Connects computers"),
    GetHint(4, "R__uter", "Router", "Directs traffic in a network"),
    GetHint(4, "Sw__t__h", "Switch", "Connects devices in a LAN"),
    GetHint(4, "Ar__ay", "Array", "Ordered collection of elements"),
    GetHint(4, "St__ck", "Stack", "Last In First Out data structure"),
    GetHint(4, "Q__eue", "Queue", "First In First Out data structure"),
    GetHint(4, "R__c__rs__on", "Recursion", "Function calling itself"),
    GetHint(4, "Va__i__ble", "Variable", "Stores data temporarily"),
    GetHint(4, "C__mp__ler", "Compiler", "Translates source code"),
    GetHint(2, "D__b__gger", "Debugger", "Helps find bugs"),
    GetHint(2, "O__er__ting S__st__m", "Operating System", "Manages hardware and software"),
    GetHint(2, "C__ch__", "Cache", "Fast small memory"),
    GetHint(2, "R__M", "RAM", "Volatile memory"),
    GetHint(2, "R__M", "ROM", "Non-volatile memory"),
    GetHint(2, "F__le", "File", "Stores data on disk"),
    GetHint(2, "D__ta__ase", "Database", "Structured data storage"),
    GetHint(2, "SQL", "SQL", "Query language for databases"),
    GetHint(2, "N__de", "Node", "Unit in a linked list or tree"),
    GetHint(10, "Ed__e", "Edge", "Connection in a graph"),
    GetHint(10, "Gr__ph", "Graph", "Set of nodes and edges"),
    GetHint(10, "Tr__e", "Tree", "Hierarchical data structure"),
    GetHint(8, "B__n__ry", "Binary", "Base 2 number system"),
    GetHint(9, "H__sh", "Hash", "Used for quick lookup"),
    GetHint(3, "F__nction", "Function", "Reusable block of code"),
    GetHint(7, "C__ass", "Class", "Blueprint for an object"),
    GetHint(3, "Ob__ect", "Object", "Instance of a class"),
    GetHint(3, "Enc__ps__lation", "Encapsulation", "Hiding internal details"),
    GetHint(7, "In__er__t__nce", "Inheritance", "Deriving from a parent class"),
    GetHint(7, "P__ly__orp__ism", "Polymorphism", "Many forms of one interface"),
    GetHint(9, "I__ter__ace", "Interface", "Defines method signatures"),
    GetHint(9, "A__str__ct", "Abstract", "Incomplete class"),
    GetHint(7, "Cl__ud", "Cloud", "Remote servers on the internet"),
    GetHint(5, "G__t", "Git", "Version control system"),
    GetHint(5, "Br__nch", "Branch", "Parallel version of code"),
    GetHint(5, "M__rg__", "Merge", "Combine code changes"),
    GetHint(5, "Re__o", "Repo", "Code repository"),
    GetHint(6, "C__mm__t", "Commit", "Save changes in git"),
    GetHint(6, "P__ll", "Pull", "Fetch latest code"),
    GetHint(6, "P__sh", "Push", "Send code to remote"),
    GetHint(6, "API", "API", "Interface between systems"),
    GetHint(6, "Th__e__d", "Thread", "Unit of CPU execution"),
    GetHint(8, "P__oc__ss", "Process", "Running instance of a program"),
]


# -- Game loop --
while player.get_total_diamonds() > 0:
    # Filter puzzles matching the player's current level
    available = [
        p for p in puzzles
        if p.get_question_level() == player.get_player_level()
    ]
    if not available:
        print("No puzzles left for your level.")
        break

    current = random.choice(available)
    print(player.get_total_diamonds())
    print(current)

    # Inner loop: try to solve the current puzzle
    while current.get_remaining_rounds() > 0:
        # Show how many hints the player has
        print(
            f"Hints: {player.get_hint_count()} "
            f"(Next costs {player.get_hint_cost()} diamonds) "
        )

        guess = input("Your answer (or type 'hint'): ").strip()

        if guess.lower() == "hint":
            # If they already purchased hints, use one
            if player.use_hint():
                print(f"Hint -> {current.get_hint()}")
            else:
                # Offer to purchase a hint
                cost = player.get_hint_cost()
                buy = input(f"No hints left. Buy one for "
                            f"{cost} diamonds? (y/n): ").strip().lower()
                if buy == "y" and player.buy_hint():
                    print("Hint purchased.")
                    player.use_hint()
                    print(f"Hint -> {current.get_hint()}")
                else:
                    print("No hint this time.")
            continue

        # Check answer
        if current.is_answer_correct(guess):
            print("Correct!")
            player.add_diamonds(1)
            player.increase_player_level()
            break
        else:
            print("Incorrect! "
                  f"Rounds left: {current.get_remaining_rounds()}")

    else:
        # Ran out of rounds for this puzzle
        print("You failed this puzzle.")

    # Show updated player stats
    print(player)

    # Remove solved/attempted puzzle so it won't repeat
    puzzles.remove(current)

print("Game Over: out of diamonds or puzzles.")

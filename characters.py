# characters.py

class Players:
    def __init__(self, name: str, level: int, diamond: int) -> None:
        self.__name = name
        self.__level = level
        self.__diamond = diamond

    def get_total_diamonds(self) -> int:
        return self.__diamond

    def get_player_level(self) -> int:
        return self.__level

    def increase_player_level(self) -> None:
        self.__level += 1

    def use_diamonds(self, amount: int) -> bool:
        """Return True if paid, False if insufficient diamonds."""
        if amount > self.__diamond:
            return False
        self.__diamond -= amount
        return True

    def add_diamonds(self, amount: int) -> None:
        self.__diamond += amount

    def __str__(self) -> str:
        return (
            f"Player: {self.__name}, Level: {self.__level}, "
            f"Diamonds: {self.__diamond}"
        )


class DiamondPlayer(Players):
    COST = 2

    def __init__(self, name: str, level: int, diamond: int) -> None:
        super().__init__(name, level, diamond)
        self.__hint_count = 1
        self.__hint_cost = self.COST

    def buy_hint(self) -> bool:
        """
        Attempt to purchase one hint at current hint cost.
        Returns True if successful, False otherwise.
        """
        if not self.use_diamonds(self.__hint_cost):
            return False

        self.__hint_count += 1
        self.__hint_cost += 1
        return True

    def get_hint_count(self) -> int:
        return self.__hint_count

    def get_hint_cost(self) -> int:
        return self.__hint_cost

    def use_hint(self) -> bool:
        """
        Consume one purchased hint.
        Returns True if a hint was available, False otherwise.
        """
        if self.__hint_count <= 0:
            return False
        self.__hint_count -= 1
        return True

    def __str__(self) -> str:
        return (
            f"{super().__str__()}, "
            f"Hints Available: {self.__hint_count}"
        )

# characters.py

class Players:
    def __init__(self, name: str, level: int, rank: str, diamond: int) -> None:
        self.__name = name
        self.__level = level
        self.__rank = rank
        self.__diamond = diamond

    def get_total_diamonds(self) -> int:
        return self.__diamond

    def get_player_level(self) -> int:
        return self.__level

    def get_player_rank(self) -> str:
        return self.__rank

    # To be used within a try except block to prevent the coding from breaking
    def use_diamonds(self, amount: int) -> None:
        if amount > self.__diamond:
            raise Exception('Insufficient diamonds')

        # Update Diamond
        self.__diamond -= amount

    def add_diamonds(self, amount: int) -> None:
        # Update Diamond
        self.__diamond += amount

    def __str__(self) -> str:
        return (
            f"Player: {self.__name}, Level: {self.__level}, "
            f"Rank: {self.__rank}, Diamonds: {self.__diamond}"
        )


class DiamondPlayer(Players):
    # Constants
    COST = 2

    def __init__(self, name: str, level: int, rank: str, diamond: int) -> None:
        super().__init__(name, level, rank, diamond)
        self.__hint_count = 0

    def buy_hint(self) -> None:
        try:
            self.use_diamonds(self.COST)
            self.__hint_count += 1
            self.COST += 1

        except Exception as e:
            print(f"Hint not Purchased: {e}")

    def get_hint_count(self) -> int:
        return self.__hint_count

    def __str__(self) -> str:
        return f"{super().__str__()}, Hints Used: {self.__hint_count}"

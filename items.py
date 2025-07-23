# items.py

class Puzzle:
    MAX_ROUNDS = 5

    def __init__(
        self,
        level: int,
        question: str,
        answer: str,
    ) -> None:
        self.__level = level
        self.__question = question
        self.__answer = answer
        self.__rounds_left = self.MAX_ROUNDS

    def get_question(self) -> str:
        return self.__question

    def get_answer(self) -> str:
        return self.__answer

    def get_question_level(self) -> int:
        return self.__level

    def is_answer_correct(self, user_input: str) -> bool:
        if user_input.lower().strip() == self.__answer.lower().strip():
            return True
        self.__rounds_left -= 1
        return False

    def get_remaining_rounds(self) -> int:
        return self.__rounds_left

    def __str__(self) -> str:
        return (
            f"Level: {self.__level}, "
            f"Question: {self.__question}, "
            f"Rounds Left: {self.__rounds_left}"
        )


class GetHint(Puzzle):
    def __init__(
        self,
        level: int,
        question: str,
        answer: str,
        hint: str
    ) -> None:
        super().__init__(level, question, answer)
        self.__hint = hint

    def get_hint(self) -> str:
        return self.__hint

    def __str__(self) -> str:
        return super().__str__()

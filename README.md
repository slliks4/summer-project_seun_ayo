# 🌍 World Puzzle

## 🎮 Game Overview

**World Puzzle** is a word-based puzzle game built using object-oriented programming (OOP) principles. Players earn diamonds by solving puzzles and can use those diamonds to get hints. As players win more rounds, they level up and increase their rank. The game also includes random bonus rounds that offer greater rewards.

---

## 🧩 Game Structure

### 🧑‍💼 Characters

#### `Player` (Base Class)
- **Attributes**: `name`, `level`, `rank`, `diamonds`
- **Methods**:
  - `get_total_diamonds()`
  - `get_player_level()`
  - `get_player_rank()`
  - `use_diamonds(amount)`
  - `add_diamonds(amount)`
  - `__str__()`

#### `DiamondPlayer` (Subclass)
- Adds: `hint_count`
- Overrides: `use_diamonds()` to buy hints
- Adds: hints tracking in `__str__()`

---

### 📚 Items

#### `Puzzle` (Base Class)
- **Attributes**: `level`, `word`, `answer`, `max_attempts`
- **Methods**:
  - `get_answer()`
  - `get_remaining_rounds()`
  - `__str__()`

#### `BonusRound` (Subclass)
- Adds: `reward_multiplier`
- Overrides: `__str__()` to show bonus rewards

---

## 🛠️ Demo in `main.py`

- Creates:
  - 1 Regular Puzzle and 1 Bonus Round
  - 1 Player and 1 DiamondPlayer
- Simulates:
  - Players solving puzzles and earning diamonds
  - Players using diamonds to get hints
  - Prints player stats and puzzle summaries

---

## ✅ Learning Outcomes

- Object-Oriented Programming
- Class Design and Inheritance
- Method Overriding
- State Management
- Simulated Game Logic

---

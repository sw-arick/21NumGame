# 21 Number Game

A command-line counting game written in Python. You and the computer take turns counting up from 1. On each turn you call out 1, 2, or 3 consecutive numbers, and whoever is forced to say **21** loses.

## Features

- Choose whether you go first or the computer does
- Computer opponent that uses a mathematical winning strategy
- Rules displayed at the start of the game
- Input validation for the move count and the first-player choice
- Clear win and lose messages

## Rules

1. Players take turns counting up from 1 to 21.
2. On your turn, you can call out 1, 2, or 3 consecutive numbers.
3. The player who is forced to call 21 loses.

## Example

```
--- 21 NUMBER GAME RULES ---
...
Do you want to go first? (y/n): n

--- Computer's Turn ---
Computer called: 1

--- Your Turn ---
Current count is: 1
How many numbers do you want to add? (1, 2, or 3): 3
You called: 2 3 4
```

## Run it locally

```bash
git clone https://github.com/sw-arick/21-number-game.git
cd 21-number-game
python main.py
```

Requires Python 3. No external libraries needed.

## The strategy

The computer always tries to leave the count at a multiple of 4. Whatever you add (1 to 3), it can add enough to land on the next multiple of 4 again, until it forces you to be the one to say 21. If you go first, the computer can always win. If you go second, you can beat it by working out the pattern yourself.

## Concepts used

- Functions to organize the game flow
- `while` loops with `try` / `except` for input validation
- The modulo operator (`%`) for the winning strategy
- Boolean flag to switch turns between player and computer

## Ideas for improvement

- Add a "play again" option
- Add difficulty levels where the computer sometimes plays randomly
- Let the player choose the target number and maximum step (for example, 31 and 1 to 4)
- Track wins and losses across rounds

## Author

[sw-arick](https://github.com/sw-arick)

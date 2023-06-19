#!/usr/bin/env python3
# connect_four.py

import numpy as np
import random

# found code ideas on compuacademy

# Starting player score board at 0
player1_score = 0
player2_score = 0

# Play game 1 time.
for i in range(1):

    # Random probability of winning between player 1 and 2
    player1_value = random.randint(1, 3)
    player2_value = random.randint(1, 3)

    # Conditions for each player to win.
    if player1_value == 1:
        print("player 1 wins.")
        player1_score = player1_score + 1  # adding to score board
    elif player2_value == 2:
        print("player 2 wins")
        player2_score = player2_score + 1
    else:
        print("It's a draw")

    input(
        "Press enter to continue."
    )  # Wait for user to press enter in terminal to proceed.

print("Game Over")
print("Player 1 score:", player1_score)
print("Player 2 score:", player2_score)


def main():
    board1 = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 2, 2, 1, 1, 0, 0],
        [0, 2, 1, 2, 2, 0, 1],
        [2, 1, 1, 1, 2, 0, 2],
    ]

    board2 = [
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 1, 0],
        [0, 1, 1, 2, 2, 2, 0],
        [2, 2, 1, 1, 1, 2, 0],
    ]

    board3 = [
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 2, 2, 0],
        [0, 1, 2, 1, 2, 2, 0],
        [0, 2, 2, 2, 1, 1, 0],
        [0, 1, 1, 2, 1, 2, 0],
    ]
    # values of each board that go with random probability of winning.
    board1 == 1
    board2 == 2
    board3 == 3


if __name__ == "__main__":
    main()

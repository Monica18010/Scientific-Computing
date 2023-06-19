from collections import defaultdict

M = defaultdict(int)


def EncodeHash(s, encoder):
    if len(s) == 9:
        M[encoder] = s
        return
    EncodeHash(s + "0", encoder)
    EncodeHash(s + "1", encoder + 3 ** (8 - (len(s))))
    EncodeHash(s + "2", encoder + 2 * (3 ** (8 - (len(s)))))


def decodeBoard(n):
    if M[n] == 0:
        print("Not a possible Encode.")
    L = list(M[n])
    L = list(map(int, L))
    return L


def checkWinner(L):
    Table = [[0 for i in range(3)] for i in range(3)]
    for i in range(3):
        for j in range(3):
            Table[i][j] = L[i * 3 + j]
    Winner = 0
    for i in range(3):
        if Table[i][0] == Table[i][1] and Table[i][1] == Table[i][2]:
            if Winner == 0:
                Winner = Table[i][0]
        if Table[0][i] == Table[1][i] and Table[1][i] == Table[2][i]:
            if Winner == 0:
                Winner = Table[0][i]
    if Table[0][0] == Table[1][1] and Table[1][1] == Table[2][2]:
        if Winner == 0:
            Winner = Table[1][1]
    if Table[2][0] == Table[1][1] and Table[1][1] == Table[0][2]:
        if Winner == 0:
            Winner = Table[1][1]
    if Winner == 0:
        return "no winner"
    elif Winner == 1:
        return "X wins"
    else:
        return "O wins"


EncodeHash("", 0)  # Calculating all possible combinations allowed
n = int(input("Put your Encoded Input: "))
L = decodeBoard(n)  # to decode board that corresponds to the encoded input given
print(checkWinner(L))


# The board list that corresponds to the board
print("The board list is: ", L)
print("The board looks like: ")

for i in range(3):
    for j in range(3):
        if L[i * 3 + j] == 0:
            print("_", end=" ")
        elif L[i * 3 + j] == 1:
            print("X", end=" ")
        elif L[i * 3 + j] == 2:
            print("O", end=" ")
    print()

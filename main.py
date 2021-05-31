import itertools
from tabulate import tabulate

positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def gameBoard():
    board = [positions[i:i+3] for i in range(0,9,3)]
    print(tabulate(board, tablefmt="grid"))
    #print('|' + str(positions[0]) + '|' + str(positions[1]) + '|' + str(positions[2]) + '|')
    #print('-------')
    #print('|' + str(positions[3]) + '|' + str(positions[4]) + '|' + str(positions[5]) + '|')
    #print('-------')
    #print('|' + str(positions[6]) + '|' + str(positions[7]) + '|' + str(positions[8]) + '|')

winner = False
nameList = []
for i in range(1, 3):
    playerName = input(f"What is Player {i}'s name? ")
    nameList.append(playerName)

counter = 0
nameCycle = itertools.cycle(nameList)
playerOne = 'X'
playerTwo = 'O'

while not winner:
  gameBoard()
  for i in range(9):
        nameToggle = next(nameCycle)
        print(f"It is your turn, {nameToggle}.")
        chosenNumber = int(input("From a number between 1-9, what number would you like to choose? "))
        if nameToggle == nameList[0]:
            positions[chosenNumber - 1] = playerOne
            counter += 1
            gameBoard()
        elif nameToggle == nameList[1]:
            positions[chosenNumber - 1] = playerTwo
            counter += 1
            gameBoard()

        if counter >= 5:
            #X
            if positions[0] == "X" and positions[1] == "X" and positions[2] == "X":
                print(f"{nameList[0]} is the winner!")
                winner = True
                break
            elif positions[3] == "X" and positions[4] == "X" and positions[5] == "X":
                print(f"{nameList[0]} is the winner!")
                winner = True
                break
            elif positions[6] == "X" and positions[7] == "X" and positions[8] == "X":
                print(f"{nameList[0]} is the winner!")
                winner = True
                break
            elif positions[0] == "X" and positions[3] == "X" and positions[6] == "X":
                print(f"{nameList[0]} is the winner!")
                winner = True
                break
            elif positions[1] == "X" and positions[4] == "X" and positions[7] == "X":
                print(f"{nameList[0]} is the winner!")
                winner = True
                break
            elif positions[2] == "X" and positions[5] == "X" and positions[8] == "X":
                print(f"{nameList[0]} is the winner!")
                winner = True
                break
            elif positions[0] == "X" and positions[4] == "X" and positions[8] == "X":
                print(f"{nameList[0]} is the winner!")
                winner = True
                break
            elif positions[6] == "X" and positions[4] == "X" and positions[2] == "X":
                print(f"{nameList[0]} is the winner!")
                winner = True
                break
            #O
            if positions[0] == "O" and positions[1] == "O" and positions[2] == "O":
                print(f"{nameList[1]} is the winner!")
                winner = True
                break
            elif positions[3] == "O" and positions[4] == "O" and positions[5] == "O":
                print(f"{nameList[1]} is the winner!")
                winner = True
                break
            elif positions[6] == "O" and positions[7] == "O" and positions[8] == "O":
                print(f"{nameList[1]} is the winner!")
                winner = True
                break
            elif positions[0] == "O" and positions[3] == "O" and positions[6] == "O":
                print(f"{nameList[1]} is the winner!")
                winner = True
                break
            elif positions[1] == "O" and positions[4] == "O" and positions[7] == "O":
                print(f"{nameList[1]} is the winner!")
                winner = True
                break
            elif positions[2] == "O" and positions[5] == "O" and positions[8] == "O":
                print(f"{nameList[1]} is the winner!")
                winner = True
                break
            elif positions[0] == "O" and positions[4] == "O" and positions[8] == "O":
                print(f"{nameList[1]} is the winner!")
                winner = True
                break
            elif positions[6] == "O" and positions[4] == "O" and positions[2] == "O":
                print(f"{nameList[1]} is the winner!")
                winner = True
                break
            else:
                continue
import math
from random import *

p_row = randint(0,3)
p_col = randint(0,3)
k_row = 1
k_col = 1
e_row = 3
e_col = 2
found = False
board = [
[" _ "," _ "," _ "," _ "],
[" _ "," _ "," _ "," _ "],
[" _ "," _ "," _ "," _ "],
[" _ "," _ "," _ "," _ "]
]
def display():
    for i in range(4):
        for j in range(4):
            if(i == p_row and j == p_col):
                print(" P ", end="")
            elif(i == k_row and j == k_col):
                if found == False:
                    print(" K ", end="")
                else:
                    print(" _ ", end ="")
            elif(i == e_row and j == e_col):
                print(" E ", end="")
            else:
                print(" _ ", end="")
        print("")
    
print(p_row)
print(p_col)
stop = False
while stop == False:
    display()
    move = input("Move: a - left, d - right, w - up, s - down: ")

    if(move == "a"):
        if(p_col - 1 < 0):
            print("cant move")
        else:
            p_col -=1
    elif(move == "d"):
        if(p_col + 1 > 3):
            print("cant move")
        else:
            p_col +=1
    elif(move == "w"):
        if(p_row - 1 < 0):
            print("cant move")
        else:
            p_row -=1
    elif(move == "s"):
        if(p_row + 1 > 3):
            print("cant move")
        else:
            p_row +=1
    
    if p_col == k_col and p_row == k_row:
        print("You pick a key")
        found = True
    elif found == False:
        print("You cant exit. Acquire the key")

    if p_col == e_col and p_row == e_row:
        if(found == True):
            print("congrats")
            stop = True

    
    



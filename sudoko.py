# solver.py
from dokusan import generators,renderers
import numpy as np
import random as ran

def generate_sudokopuzz(avgrank):
    sudoko = generators.random_sudoku(avg_rank=avgrank)
    sudoko1=np.array(list(str(sudoko)))
    sudoko3= sudoko1.astype('int')
# board=[[0,0,1,5,0,7,0,0,0],
#  [0,0,0, 0, 0, 6, 0, 4, 0],
#  [4,0, 0, 9, 2, 0, 0, 1, 0],
#  [1,0,3, 0, 0, 0 ,5 ,0, 6],
#  [0 ,4 ,0 ,0 ,0 ,0 ,3 ,0 ,0],
#  [0 ,7, 9, 0, 0 ,0 ,0, 0, 0],
#  [0 ,0 ,0 ,6 ,0 ,4 ,7 ,0 ,0],
#  [9 ,3, 0, 7, 8 ,0 ,0,0, 0],
#  [0 ,0 ,5 ,3 ,0, 0 ,0 ,0 ,8]]
    solving_board=sudoko3.reshape(9,9)
    solved_board=sudoko3.reshape(9,9)
    return(solving_board,solved_board)


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

def create_empty_arr(s,d):
    s =  [[0] * 9] * 9  
    p=np.array(s) 
    for i in range(9):
        for j in range(9):
            p[i][j]=d[i][j];
    s=d

    return p


def checking_function(s,d):
    flag=0 
    if(s.all()==d.all()):
        flag=flag+1
        print("CONGRATULATIONS YOU'VE SOLVED THE SUDOKO PUZZLE")
        return flag
    else:
        print("TRY AGAIN")
        return flag






#main function

difficultylevel=int(input("ENTER THE DIFFICULTY-\n1:Easy\n2.Medium\n3.Hard \n"))
if(difficultylevel==1):
    diff=ran.randint(0, 100)
elif(difficultylevel==2):
    diff=ran.randint(101,200)
else:
    diff=ran.randint(200,500)


solving_board,solved_board=generate_sudokopuzz(diff)
s=[[]]
s=create_empty_arr(s,solving_board)
# print_board(s)
# print("\n\n-------------------------------------------")
# print_board(s)
# solved_board1=solving_board
solve(solved_board)
# print("\n\n-------------------------------------------")
# print_board(solving_board)
# print("\n\n-------------------------------------------")

print_board(solved_board)
print("\n\n-------------------------------------------")
print_board(s)
print("\n\n-------------------------------------------")

while(True):
    print("Select from the following options:\n1.Enter value in the grid\n2.Check (if completed with solving)\n3.exit")
    choice=int(input())
    if(choice==1):
        print("Enter the coordinates in the grid x and y")
        x_cord=int(input("Enter the X coordinate "))
        y_cord=int(input("Enter the Y coordinate "))
        number=int(input("Enter the number "))
        if(number>9 or number<1):
            print("Enter valid number (number should be between 1-9")
            continue
        if(s[x_cord-1][y_cord-1]>0):
            print("You cannot change the pre-existing values")
            continue
        s[x_cord-1][y_cord-1]=number
        print_board(s)
    if(choice==2):
        #call checking function
        flag=checking_function(s,solved_board)
        if(flag==0):
            continue
        else:
            break
        pass
    if(choice==3):
        break;

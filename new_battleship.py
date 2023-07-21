### trying to understand for loops for thew battle ship thing
from random import*

#Board size is inputed and printed
my_grid=[]
#CPU Grid
cpu_grid=[]

#Board size
while True:
    try:
        board_size = int(input("What size board do you want? enter one interger: "))
        ship_size = 2
        if ship_size > board_size:
            print("Ship size cannot be larger than the board size. Please enter valid values.")
        elif board_size == 0 or board_size <=1:
            print ("You wanna play battleship with no grid??? Try again...")
        elif ship_size <1:
            print("Ship size must be 1 or larger....or just drown.")
        else:
            break
    except:
        print("That's not a single integer")
        
    
print("Sink Or Swim - Battleship")


for x in range(board_size):
    my_grid.append(["0"]*board_size)

def print_grid(my_grid):  
    for row in my_grid:
        print((" ").join(row))        
print_grid(my_grid)
  

while True:
    cpu_board_size = board_size
    cpu_ship_size = ship_size
    break
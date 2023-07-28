### trying to understand for loops for thew battle ship thing
from random import*

def print_grid(grid):
    print(" ".join(["C"] + [str(i + 1) for i in range(board_size)]))  # Print column labels
    for row_num, row in enumerate(grid, 1):
        print(" ".join([str(row_num)] + row))        

def Guesses():
    for guess in range(5):
        while True:
            try:
                guess_column = int(input("What column do you want to hit? ")) - 1
                guess_row = int(input("What row do you want to hit? ")) - 1
                break
            except ValueError:
                print("Not a coordinate on the map")

            if guess_row == ship_row - 1 and guess_column == ship_column - 1:
                print("You hit it!")
                break
            elif guess_column >= board_size or guess_row >= board_size or guess_column < 0 or guess_row < 0:
                print("Out of bounds")
            else:
                print("Miss")
            if guess == 4:
                print("Game over")
            guess += 1

    print("The ship was located at:")
    for i in range(ship_size):
        my_grid[ship_row - 1 + i][ship_column - 1] = "S"
        print("C:", ship_column,"R:", ship_row + i) 





############################################################ --ACTUAL GAME-- ################################################################

my_grid=[]

while True:
    try:
        ship_name = input("What would you like to name your ship:  ")
        board_size = 10
        ship_size = int(input("What size ship do you want? Enter a single integer: "))
        if ship_size > board_size:
            print("Ship size cannot be larger than the board size. Please enter valid values.")
        elif board_size <=1:
            print ("You wanna play battleship with no grid basically... Try again")
        elif ship_size <1:
            print("Ship size must be 1 or larger....or just drown.")
        else:
            break
    except:
        print("That's not a single integer")
        
    
print("Sink Or Swim - Battleship")


#Creates the game grid
for x in range(board_size):
    my_grid.append(["0"]*board_size)
print_grid(my_grid)


while True:
    cpu_board_size = board_size
    cpu_ship_size = ship_size
    break



user_input=input("Enter 1 to just attack cpu (not vice versa). Enter 2 for cpu attack you: ")

while True:
    if user_input == '1':  

    #If player wants random ship placement
        ship_name = input("What would you like to name your ship:  ")  
        ship_row = randint(1, board_size - ship_size + 1)
        ship_column = randint(1, board_size - ship_size + 1)

        Guesses()
        break

    elif user_input == '2':
            # Allows user to place their ship

        while True:
            try:
                ship_name = input("What would you like to name your ship:  ")
                ship_row = int(input("Enter the row for ship placement (1 to {}): ".format(board_size - ship_size + 1))) - 1
                ship_column = int(input("Enter the column for ship placement (1 to {}): ".format(board_size - ship_size + 1))) - 1
                if 0 <= ship_row <= board_size - ship_size and 0 <= ship_column <= board_size - ship_size:
                    break
                else:
                    print("Invalid coordinates. Please enter valid values.")
            except ValueError:
                print("Invalid input. Please enter integer values.")

        print("The ship has been placed on the grid by the user.")
        print("Ship's location: R: {} , C: {}".format(ship_row + 1, ship_column + 1))
        for i in range(ship_size):
            my_grid[ship_row + i][ship_column] = "S"
            print(ship_row + 1 + i, ship_column + 1)
        print_grid(my_grid)
        break

    else:
        print("Invalid input. Please enter either 1 or 2.")
        break


cpu_grid = []  # Reset the cpu_grid for each game round

ship_row = randint(1, board_size - ship_size + 1)
ship_column = randint(1, board_size - ship_size + 1)

print("\t")
print("Prepare for War")
print("\t")

for x in range(board_size):
    cpu_grid.append(["0"] * board_size)

while True:
    for guess in range(5):
        while True:
            try:
                guess_column = int(input("What column do you want to hit? ")) - 1
                guess_row = int(input("What row do you want to hit? ")) - 1
                break
            except ValueError:
                print("Not a coordinate on the map")

            if guess_row == ship_row - 1 and guess_column == ship_column - 1:
                print("You hit it!")
                cpu_grid[guess_row][guess_column] = "X"
                print_grid(cpu_grid)
                break
            elif guess_column >= board_size or guess_row >= board_size or guess_column < 0 or guess_row < 0:
                print("Out of bounds")
            elif cpu_grid[guess_row][guess_column] == 'M':
                print("You already blew up nothing try again.")
            else:
                print("User Miss")
                cpu_grid[guess_row][guess_column] = "M"
                print_grid(cpu_grid)
            if guess == 4:
                print("Game over")
            guess += 1


    
    print("The ship was located at:")
    for i in range(ship_size):
        cpu_grid[ship_row - 1 + i][ship_column - 1] = "S"
        print("C:", ship_column, "R:", ship_row + i)
    break

for c_guess in range(5):
    computer_column = randint(0, board_size - 1)
    computer_row = randint(0, board_size - 1)

    if computer_row == ship_row - 1 and computer_column == ship_column - 1:
        print("CPU hit your ship!")
        my_grid[computer_row][computer_column] = "X"
        
        break
    else:
        print("CPU Miss")
        my_grid[computer_row][computer_column] = "M"

        print("CPU's guess:")
        print_grid(my_grid)

    if c_guess == 4:
        print("Game over")

        print("The ship was located at:")
        for i in range(ship_size):
            cpu_grid[ship_row - 1 + i][ship_column - 1] = "S"
            print("C:", ship_column, "R:", ship_row + i)
        print_grid(cpu_grid)
    break



### trying to understand for loops for thew battle ship thing
from random import*

#Board size is inputed and printed
my_grid=[]
#CPU Grid
cpu_grid=[]

while True:
    try:
        board_size = int(input("What size board do you want? enter one interger: "))
        ship_size = int(input("What size ship do you want? Enter a single integer: "))
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

 
def battleship():
     
    user_input=input("Enter 1 to just kill cpu (not vice versa). Enter 2 for cpu kill you: ")

    while True:
        if user_input == '1':
            
            #If player wants random ship placement    
            ship_row = randint(1, board_size - ship_size + 1)
            ship_column = randint(1, board_size - ship_size + 1)



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

            Guesses()
            
            break
        elif user_input == '2':
            # Allows user to place their ship

            while True:
                try:
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

        else:
            print("Invalid input. Please enter either 1 or 2.")
            battleship()


        






        def playgame():
            cpu_board_size = board_size
            cpu_ship_size = ship_size
            

            cpu_ship_row = randint(1,cpu_board_size - cpu_ship_size)
            cpu_ship_column = randint(1,cpu_board_size - cpu_ship_size)

            #ship_row = int(1, board_size - ship_size + 1)
            #ship_column = int(1, board_size - ship_size + 1)

            print("Prepare for War")
            print("\t")

            for x in range(cpu_board_size):
                cpu_grid.append(["0"]*cpu_board_size)
            def print_grid(cpu_grid):
                for row in cpu_grid:
                    print((" ").join(row)) 
            print_grid(cpu_grid)

            for (guess) in range(5):
                while True:
                    try:
                        guess_column = int(input("What column do you want to hit? ")) - 1
                        guess_row = int(input("What row do you want to hit? ")) - 1

                        computer_column = randint(1, len(my_grid))
                        computer_row = randint(1, len(my_grid))
                        break
                    except ValueError:
                        print("Not a coordinate on the map")

                if guess_row == cpu_ship_row - 1 and guess_column == cpu_ship_column - 1:
                    print("You hit it!")
                    cpu_grid[guess_column][guess_row] = "X"
                    print_grid(cpu_grid)
                    
                    if guess_row == ship_row - 1 and guess_column == ship_column - 1:
                        print("CPU hit your ship!")
                        my_grid[guess_row][guess_column] = "X"
                        break
                    break
                elif guess_column >= board_size or guess_row >= board_size or guess_column < 0 or guess_row < 0:
                    print("Out of bounds")
                    
                    if computer_column > len(my_grid) or computer_row > len(my_grid):
                        print("cpu out of bounds")
                elif  guess_row == cpu_ship_row - 1 and guess_column == cpu_ship_column - 1 =='M':
                    print("You already blew up nothing try again.")
                else:
                    print("User Miss")
                    cpu_grid[guess_column][guess_row] = "M"
                    print_grid(cpu_grid)

                    cpu_guess_column = randint(1, board_size - 1)
                    cpu_guess_row = randint(1, board_size - 1)

                    if cpu_guess_row == ship_row - 1 and cpu_guess_column == ship_column - 1:
                        print("CPU hit your ship!")
                        my_grid[cpu_guess_row][cpu_guess_column] = "X"
                    else:
                        print("CPU Miss")
                        my_grid[cpu_guess_row][cpu_guess_column] = "M"


                if guess == 4:
                    print("Game over")
                guess +=1
                exit()

        


        playgame()


battleship()






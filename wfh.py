### trying to understand for loops for thew battle ship thing
from random import*

#Board size is inputed and printed
my_grid=[]
while True:
    try:
        board_size = int(input("What size board do you want? enter one interger please?: "))
        ship_size = int(input("What size ship do you want? Enter a single integer, please: "))
        if ship_size > board_size:
            print("Ship size cannot be larger than the board size. Please enter valid values.")
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
  
 
def battleship():
     
    user_input=input("Enter 1 if you would like the ship to be randomized. Enter 2 if you would like to place it yourself: ")

    while True:
        if user_input == '1':
            
            #If player wants random ship placement    
            def random_r(board_size):
                return randint(0, len(board_size)-1)
            def random_c(board_size):
                return randint(0, len(board_size[0])-1)

            ship_row = random_r(my_grid)
            ship_column = random_c(my_grid)


            def Guesses():
                    for guess in range (5):
                        
                        while True:
                            try:
                                guess_column = int(input("what column do you want to hit: "))
                                guess_row = int(input('what row do you want to hit: '))
                                break
                            except ValueError:
                                print("Not a coordinate on map")
                            
                                
                        if (guess_row -1) == ship_row and (guess_column -1) == ship_column:
                            print('you hit it!')
                            break            
                        elif guess_column > board_size or guess_row > board_size:
                            print ("out of bounds")
                        else:
                            print ("miss")
                        if guess == 5 :
                            print('Game over') 
                        guess = guess + 1        

                    print("The ship was located at:")
                    print(ship_column , ship_row)
            Guesses ()
            
            break
        elif user_input =='2':
            #Allows user to place their ship
            while True:
                try:
                    ship_row = int(input("Enter the row for ship placement (0 to {}): ".format(board_size - 1)))
                    ship_column = int(input("Enter the column for ship placement (0 to {}): ".format(board_size - 1)))
                    if 0 <= ship_row < board_size and 0 <= ship_column < board_size:
                        break
                    else:
                        print("Invalid coordinates. Please enter valid values.")
                except ValueError:
                    print("Invalid input. Please enter integer values.")

            print("The ship has been placed on the grid by the user.")
            print("Ship's location: ", ship_column, ship_row)
            break
            
        else:
            print("Invalid input.Please enter either 1 or 2.")
            battleship()

battleship()

                
    
        
        
     
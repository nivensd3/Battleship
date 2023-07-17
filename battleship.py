### trying to understand for loops for thew battle ship thing
from random import*

#Board size is inputed and printed
my_grid=[]
while True:
    try:
        board_size = eval(input("What size board do you want? enter one interger please?: "))
        break
    except NameError:
        print("That's not a number")
        
    
print("Sink Or Swim - Battleship")

for x in range(board_size):
    my_grid.append(["0"]*board_size)

def print_grid(my_grid):  
    for row in my_grid:
        print((" ").join(row))        
print_grid(my_grid)
  
  
  

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


                
    
        
        
     


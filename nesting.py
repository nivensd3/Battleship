### trying to understand for loops for thew battle ship thing
from random import*

#Board size is inputed and printed
my_grid=[]
while True:
    try:
        board_size = eval(input("What size board do you want? enter one interger please?:  "))
        
    except: 
        NameError
        print("That's not a number")
    if type(board_size) == int:
        break

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

 


 
 
 
def Guesses():
        for guess in range (5):
            guess_column = eval(input("what column do you want to hit: "))
            guess_row = eval(input('what row do you want to hit: '))
            if type(guess_column or guess_row) == str:
                print ("Please enter a number")
                guess = guess + 0 
                break
                
            btl_ship = guess_column and guess_row
            if guess_column > board_size or guess_row > board_size:
                print ("out of bounds")
                
            elif guess_column and guess_row == btl_ship:
                
               print('you hit it!')
        if guess == 4 :
            print('Game over') 
        guess = guess + 1 
        
    
        
Guesses ()
        
        
     


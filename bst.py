from random import*

#Board size is inputed and printed
my_grid=[]
board_size = eval(input("What size board do you want? enter one interger please?:  "))

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














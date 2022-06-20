from calendar import c
import random

from sqlalchemy import false

def game_win(comp, player):
    if comp == player:
        return None
    elif comp == 's':
        if player == 'w':
            return False
        elif player == 'g':
            return True
    elif comp == 'w':
        if player == 's':
            return True
        elif player == 'g':
            return False                
    elif comp == 'g':
        if player == 's':
            return False
        elif player == 'w':
            return True      


print("Computer Turn: Snake(s) Water(w) or Gun(g)?")
random_no = random.randint(1,3)
if random_no == 1:
    comp = 's' 
elif random_no == 2:
    comp =  'w' 
elif random_no == 3:
    comp = 'g'

player = input("Your Turn: Snake(s) Water(w) or Gun(g)?")    

a=game_win(comp, player)
if a== None:
    print(" The Game is Tie.")
elif a:
    print("You Win!")
else:
    print("You Lose!")       

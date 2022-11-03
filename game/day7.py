
from random import *


def RPS ():
    UserChoice=input("To play, type: Rock, Paper, or Scissors ")
    if UserChoice != 'Rock' or 'Paper' or 'Scissors':
        print("Invalid selection, please type Rock, Paper, or Scissors")
    ComputerChoice = ['Rock','Paper','Sciscssors']
    print (ComputerChoice[randint(0,2)])
        
RPS()
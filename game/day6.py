
#import pygame


from random import *

myList = ['shoe','sock','shirt','pants']

def randomClothing():
    return myList[randint(0,3)]

print (randomClothing())

# importing from turtle library
from turtle import * 

from random import randint
myColors=['red','green','blue']
def rand_color():
    return myColors[randint(0,2)]

def rand_num(x,y):
    return(randint(x,y))
# sets the color and outline and begins to draw outline
color(rand_color())
begin_fill()
# this means that the cursor will move foward an ammount inbetween those 2 numbers
# and the closer they are the more accurate the exact shape because there is less possibilites for 
# rand_num to choose from
while True:
    forward(rand_num(100,100))
#left(x) is the angle the the cursor makes for the next line    
    left(135)
#this means that if the cursor returns to the origional location, it stops and fills in the outline
    if abs(pos()) < 1:
        break
end_fill()
done()

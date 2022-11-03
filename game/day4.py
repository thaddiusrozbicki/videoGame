
# login=input("Type Begin or Great")
# if login == "Begin" or login == "Great":
#     print("on")
# else: print("Please try again")
   


# importing from turtle library
from turtle import * 
# sets the color and outline and begins to draw outline
color('red','yellow')
begin_fill()
# 
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

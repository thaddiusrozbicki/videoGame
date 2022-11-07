# for i in range (3):
#     x=i
#     print(x+x*i)

def factorial(x):
    if x>1:
        return(x*factorial(x-1))
    else:
        return(x)
num=3

print ('the factorial of ', num, 'is', factorial(num))

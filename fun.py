print('welcome the world of alainans ')
# Python program to
# demonstrate accessing of
# variables of nested functions


def fun1():
    pass
fun1()    

#function with  parameters 
def add(num1:int,num2:int) ->int:
    result =num1+num2
    return result
num1,num2 = 23,20
ans = add(num1,num2)
print(f"the addition of num1 and num2 is {num1},{num2} is {ans}")
#some more functions 
def is_prime(n):
    if n in [2, 3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True
print(is_prime(78), is_prime(79))
    
'''def factorial(fact):
    product =  1
    for i in range(n):
        product = product *(i+1)
    return product  '''

from math import factorial


def factorial_recursive(n):
    return n * factorial_recursive(n-1)

    
n= int(input("Enter the Number\n"))

print(factorial(n))
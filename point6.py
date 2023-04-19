'''
Given an n natural number and an x real number, calculate n to the power of x (using for loops).
'''
x:float = float(input("Enter an integer as the base of a power: "))
n:int = int(input("Enter an integer as a power of x: "))
c = x
for i in range(1, n):
    x *= c
print(x)
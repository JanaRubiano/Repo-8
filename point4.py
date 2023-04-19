'''
Print the numbers from 1 to an n natural number, each with its factorial.
'''
num:int = int(input("Enter an integer: "))
x = 1
for y in range(1, num+1):
     x *= y
     print(y, x)
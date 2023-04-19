'''
calculate the value of 2 to the power of n (using for loops).
'''
num:int = int(input("Enter an integer: "))
for i in range(num+1):
    x = 2**i
print(x)
# 1
for num in range(1, 101):
    print(num, num**2)
#2
for num in range(1, 1000, 2):
    print(num)
    
for num in range(2, 1001, 2):
    print(num)
    
#3
num:int = int(input("Enter an integer: "))
for num in range(num, 1, 1):
    if num % 2 == 0:
        print(num)
        
#4
num:int = int(input("Enter an integer: "))
x = 1
for y in range(1, num+1):
     x *= y
     print(y, x)
    
#5
num:int = int(input("Enter an integer: "))
for num in range(1, n+1):
    print(2**num)
    
#6
n:int = int(input("Enter an integer: "))

#7
for i in range(1, 10):
    mt = [i*j for j in range(1, 11)]
    print(mt)
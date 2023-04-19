'''Print the even numbers in descending order that are less or equal to n >= 2.
'''
num:int = int(input("Enter an integer: "))
for num in range(num, 1, -1):
    if num % 2 == 0:
        print(num)
'''
The first input is a real number x, the second input is an integer n.
x is the function's input and n the number of repetition the series will make.
The outputs are: the value of e^x calcultaed by the compputer with the math module, 
the Maclaurin series approximation of e^x, the difference between both previous values, 
and the number n that was needed to calculate the answer with less than a 0.1% error.
'''
import math
def point8(x:float, n:int) -> float:
    real = math.exp(x)
    aprox = 1
    error_limit = "Not enough to get an approximation under 0.1% of error"
    for i in range(1, n+1):
        aprox += (x**i)/math.factorial(i)
        if round(aprox, 4) == round(real, 4):
            error_limit = i
            break
    diff = real - aprox
    return f"The real value is: {real}\nThe Maclaurin series approximation is: {aprox}\nThe difference between the real and the approximated value is: {diff}\nThe value for n when there is an error of less than 0.1% is: {error_limit}"

if __name__ == "__main__":
    x = float(input("Enter a real number: "))
    n = int(input("Enter an integer: "))
    res = point8(x, n)
    print(res)
'''
The first input is a real number x, the second input is an integer n.
x is the function's input and n the number of repetition the series will make.
The outputs are: the value of arctangent(x) calcultaed by the compputer with the math module, 
the Maclaurin series approximation of arctangent(x), the difference between both previous values, 
and the number n that was needed to calculate the answer with less than a 0.1% error.
'''
import math
def point9(x:float, n:int) -> float:
    real = math.atan(x)
    aprox = 0
    error_limit = "Not enough to get an approximation under 0.1% of error"
    for i in range(n+1):
        aprox += ((-1)**i) * ((x**(2*i+1)) / (2*i+1))
        if round(aprox, 3) == round(real, 3):
            error_limit = i
            break
    diff = real - aprox
    return f"The real value is: {real}\nThe Maclaurin series approximation is: {aprox}\nThe difference between the real and the approximated value is: {diff}\nThe value for n when there is an error of less than 0.1% is: {error_limit}"

if __name__ == "__main__":
    x = float(input("Enter a natural number between -1 and 1: "))
    n = int(input("Enter an integer: "))
    res = point9(x, n)
    print(res)
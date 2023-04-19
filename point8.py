import math
def point8(x:float, n:int) -> float:
    real = math.exp(x)
    aprox = 0
    error_limit = "Not enough to get an approximation under 0.1% of error"
    for i in range(n+1):
        aprox += (x**i)/math.factorial(i)
        if round(aprox, 3) == round(real, 3):
            error_limit = i
            break
    diff = real - aprox
    
    return f"The real value is: {real}\nThe Maclaurin series approximation is: {aprox}\nThe difference between the real and the approximated value is: {diff}\nThe value for n when there is an error of less than 0.1% is: {error_limit}"

if __name__ == "__main__":
    x = float(input("Enter a real number: "))
    n = int(input("Enter an integer: "))
    res = point8(x, n)
    print(res)

    
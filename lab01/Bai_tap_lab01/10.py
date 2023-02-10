Program to calculate the value
of f(x)

where f(x) = log4x + logx2
import the math module
import math

function to calculate the value of f(x)
def calculateFx(x): f_x = math.log(x, 4) + math.log(x**2, x) return f_x

Driver Program
x = int(input("Enter the value of x: "))

Calling the function
result = calculateFx(x)

Printing the result
print("The value of f(x) is", result)
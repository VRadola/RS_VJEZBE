import math

faktorijeli = {broj: [math.factorial(i) for i in range(1, broj + 1)] for broj in range(1, 11)}
print(faktorijeli)
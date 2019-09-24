import math

num = float(input("Digite um número: "))
int = math.trunc(num)
print(f"O número {num} tem a porção inteira {int}.")

# ou

from math import trunc

num = float(input("Digite um número: "))
print("O número {} tem a porção inteira {}.".format(num, trunc(num)))

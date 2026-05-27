import math

n = 6
modi_gradini = 0

D = n // 2

while D >= 0:
    d = n - (2 * D)
    modi_gradini += math.factorial(D + d) // (math.factorial(D) * math.factorial(d))
    D -= 1

print(modi_gradini)
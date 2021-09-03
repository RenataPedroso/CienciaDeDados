import math

primos = []

def primo(x):
    for n in range(1, x+1):
        div = 0
        for i in range(1, n+1):
             if(n%i == 0):
                 div = div + 1
        if (div == 2):
             primos.append(n)
    print(primos)
primo(100)

log_numeros_primos = []

for numero in primos:
    log_numeros_primos.append(math.log(numero))

print(log_numeros_primos[9:19])
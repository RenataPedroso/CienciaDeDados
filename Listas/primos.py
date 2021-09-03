import math

### função que identifica se o número é primo
def primo(n):
    if (n < 2):
        return False
    
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

###função que adiciona os primos na lista  
def nPrimos(n):
    primos = []
    x = 2
    while (len(primos) < 25):
        if primo(x):
            primos.append(x)
        x += 1
    return primos

primos = nPrimos(100)
print(primos)
log_numeros_primos = []

for numero in primos:
    log_numeros_primos.append(math.log(numero))

print(log_numeros_primos[9:19])
import math

#criando a lista de primos
primos = []


#função que irá descobrir se é primo e adicionar à lista de primos até que o item da linha 17 seja satisfeito
def primo(x):
    for n in range(1, x+1): #esse for irá adicionar 1 a cada número dependendo do valor na linha 17
        div = 0 #divisor
        for i in range(1, n+1):
             if(n%i == 0): 
                 div += 1 #adiciona 1 ao divisor
        if (div == 2): #se o divisor for igual a 2
             primos.append(n) #adiciona n a lista de primos
    print(primos) #print o resultado da lista de primos
primo(100) #define o máximo de números a serem analisados pela função

log_numeros_primos = [] #lista de log dos primos

for numero in primos:
    log_numeros_primos.append(math.log(numero)) #realiza o log dos primos e adiciona a lista de log de primos

print(log_numeros_primos[9:19]) #printa os logs de 10 a 20
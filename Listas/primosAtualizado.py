import math

#criando a lista de primos
primos = []


#função que irá descobrir se é primo e adicionar à lista de primos até que o item da linha 17 seja satisfeito
def primo(x):
    for n in range(1, x+1): #esse for irá adicionar 1 a cada número até chegar ao valor máximo de x
        div = 0 #divisível
        for i in range(1, n+1): #esse for irá analisar todas as possibilidades possíveis de divisão
             if(n%i == 0): #se o resto da divisão do número analisado por todas as possibilidades
                 div += 1 #adiciona 1 ao divisor
        if (div == 2): #se o divisor for igual a 2, ou seja, se o número analisado for divisível somente duas vezes
             primos.append(n) #adiciona o número a lista de primos
    print(primos) #print o resultado da lista de primos
primo(100) #define o máximo de números a serem analisados pela função

log_numeros_primos = [] #lista de log dos primos
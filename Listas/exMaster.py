'''Crie uma lista com todos os número primos até  100 
Crie uma lista vazia chamada log_numeros_primos
Crie um for loop para cada item da lista de números primos e peça
    para calcular o log do item e adicioná-lo à lista log_numeros_primos
Imprima todos os items do décimo até o vigésimo da lista log_numeros_primos (cuidado com indexação não-inclusiva)'''

import math

numeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

log_numeros_primos = []

for numero in numeros_primos:
    log_numeros_primos.append(math.log(numero))

print(log_numeros_primos[9:19])

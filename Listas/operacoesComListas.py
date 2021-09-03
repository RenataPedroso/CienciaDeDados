unidades = []

'''Adicionando itens a lista'''
unidades.append('Memorial')
unidades.append('Vergueiro')
unidades.append('Vila Maria')
unidades.append('Santo Amaro')
'''Adicionando em uma posição especifica'''
unidades.insert(2, 'Guarulhos')
'''Removendo unidades'''
unidades.remove('Vila Maria')

unidades.sort() ###ordenar por ordem crescente
print(unidades)
print("")
unidades.reverse() ###ordenar em ordem descrescente
print(unidades)
print("")
print(len(unidades)) ###tamanho da lista
print("")
print(unidades.count('Memorial')) ###procurar por duplicados
print("")

'''Como tirar todos os itens duplicados?'''
unidades.append('Vergueiro')
print(unidades)
set(unidades)
unidades_nduplicadas = list(set(unidades)) ###para tirar as duplicadas precisamos criar outra lista
print(unidades_nduplicadas)

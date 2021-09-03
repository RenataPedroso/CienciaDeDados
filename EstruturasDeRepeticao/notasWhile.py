'''Ler a nota de 5 alunos e realizar média entre elas'''

count = 1 
soma = 0
while (count < 6):
  valor = float(input(f"Valor {count}: "))
  soma += valor
  count += 1
print('Soma: ', soma, 'Média: ', soma/(count-1))
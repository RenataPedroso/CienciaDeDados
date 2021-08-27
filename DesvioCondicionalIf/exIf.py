'''
Designe uma variável x com o valor  8 
Designe uma variável y com o valor  15 
Crie um desvio condicional:
que deve imprimir "Ao menos uma das condições foi satisfeita" se x maior que  3  ou y é número par
ou imprimir "Nenhuma condição foi satisfeita" se x menor ou igual a  3  e y é número ímpar
'''

x = 8
y = 15

if ((x>3) or (y%2 == 0)):
  print("Ao menos uma das condições foi satisfeita")
if ((x <= 3) and (y%2 != 0)):
  print("Nenhuma condição foi satisfeita")

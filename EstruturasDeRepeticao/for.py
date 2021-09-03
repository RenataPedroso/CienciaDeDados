frase = 'Mais vale um pássaro na mão do que dois voando.'
for letra in frase:
  if (letra =="a" or letra =="á"):
      letra = "X"
  print(letra, end=" ")
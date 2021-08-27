qtde = int(input("Quantidade de alunos: \n"))
for x in range(0, qtde, 1):
    av1 = float(input("Informe AV1: \n"))
    assert av1 <= 10, "A nota AV1 deve ser entre 0 e 10"
    
    av2 = float(input("Informe AV2: \n"))
    assert av2 <= 10, "Digite uma nota entre 0 e 10"
    
    media = (av1 + av2) / 2
    print("A média do aluno foi de: ", media)
print("Fim do Programa")
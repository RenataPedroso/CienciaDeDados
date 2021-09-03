repetir = "S"
while (repetir=="S" or repetir=="s"):
    av1 = float(input("Informe AV1: \n"))
    assert av1 <= 10, "A nota AV1 deve ser entre 0 e 10"
    
    av2 = float(input("Informe AV2: \n"))
    assert av2 <= 10, "A nota AV2 deve ser entre 0 e 10"

    av3 = float(input("Informe AV2: \n"))
    assert av2 <= 10, "A nota AV2 deve ser entre 0 e 10"

    av4 = float(input("Informe AV2: \n"))
    assert av2 <= 10, "A nota AV2 deve ser entre 0 e 10"

    av5 = float(input("Informe AV2: \n"))
    assert av2 <= 10, "A nota AV2 deve ser entre 0 e 10"
    
    media = (av1 + av2 + av3 + av4 + av5) / 5
    print("Média do aluno foi de: \n", media)
    
    repetir = input("Digite `S` caso deseje calcular nova média ou outro valor caso contrário")
print("Fim do Programa")
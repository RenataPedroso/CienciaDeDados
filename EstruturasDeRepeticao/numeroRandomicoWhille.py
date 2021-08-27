from random import randint

numero_aleatorio = randint(0, 10)
palpites_restantes = 3

while(palpites_restantes > 0):
    palpite = int(input("Qual é o seu palpite? tente um número entre 0 e 10 \n"))
    assert palpite >= 0 and palpite <= 10, "Coloque um número inteiro entre 0 e 10"
    
    if numero_aleatorio == palpite:
        print("Você acertou!")
        break 

    palpites_restantes = palpites_restantes -1

    if (palpites_restantes == 0):
        print("Você perdeu todas suas chances :(")

print("Você errou! Tente de novo")
print("O número aleatório era: ", numero_aleatorio)
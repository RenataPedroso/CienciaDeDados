#não definimos o tipo de retorno da função em python

def exemplo(parametro):
    print(parametro)
exemplo('Renata Pedroso')

def soma(valor1, valor2):
    return print('O número 1 é: ', valor1), print('O número 2 é: ', valor2), print('A soma deles é: ', valor1 + valor2)
soma(10,20)

def operacoes(valores):
    return [
        print('A soma é: ', sum(valores)),
        print('A média é: ', sum(valores)/len(valores)),
        print('O menor valor é: ', min(valores)),
        print('O maior valor é ', max(valores))
    ]

def parImpar(numero):
    if (numero%2) == 0: print('O número', numero, 'é Par')
    else:
        print('O número', numero, 'é Impar')
parImpar(4)
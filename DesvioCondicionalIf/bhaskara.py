continua = "S"

while(continua == "S" or "s"):
    a = float(input("Informe o valor de a: \n"))
    
    if (a == 0):
        print("O valor de a precisa ser diferente de 0")
        continua = input("Se deseja continuar com outro valor de 'a' digite 'S' ou 's': ")
    else:
        b = float(input("Informe o valor de b: \n"))
        c = float(input("Informe o valor de c: \n"))

        delta = (b ** 2) - 4 * a * c
        if (delta < 0):
            print("não há solução real")
        else:
            x1 = (-b - (delta ** 0.5))/(2 * a)
            x2 = (-b + (delta ** 0.5))/(2 * a)
            print("X1 = ", x1)
            print("X1 = ", x2)
            break
print("Fim do Programa!")        
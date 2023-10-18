from conversor import FparaC,CparaF

while True:

    print('\n\t\t\t -- Conversor de temperatura --\n')


#menu
    print("1. De F para C")
    print("2. De C para F")
    print("3. sair")


    op = int(input("Opção: "))

    if op == 1:
        print("De F para C")

        v1 = int(input("Informe o grau em F: "))


        total = FparaC(v1)

        print("esse valor de F para C é: {:.2f}".format(total))


    elif op == 2:
        print("De C para F")

        v1 = int(input("Informe o grau em C: "))


        total = CparaF(v1)

        print("esse valor de C para F é: {:.2f}".format(total))




    elif op == 3:
        print("Até mais!")
        break
    else:
        print("Erro: Esse número de opção não existe")
        #Tratamento de erro
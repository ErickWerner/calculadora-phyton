num = int(input("Digite um número positivo: "))

if num <0:
    print("O número não é positívo")
else:
    print(f"Os divisores do número {num} são:")

    for i in range (1,num + 1):
        if num % i == 0:
            print (i)
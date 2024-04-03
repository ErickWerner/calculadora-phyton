# Calculadora Phyton

while True: 
    operacao = int (input("--- | Menu Calculadora | --- \n 1 - Somar \n 2 - Subtrair \n 3 - Multiplicar \n 4 - Dividir \n 0 - Sair \n Digite sua opção: "))
    
    if operacao == 0:
        print ("Encerrando a calculadora...")
        break

    valor_um = int (input("Digite o primeiro número: "))
    valor_dois = int (input("Digite o segundo valor: "))

    soma = valor_um + valor_dois
    sub = valor_um - valor_dois
    multi = valor_um * valor_dois
    div = valor_um / valor_dois

    if operacao == 1:
        print (f"{valor_um:.0f} + {valor_dois:.0f} = {soma:.0f}")
    elif operacao == 2:
        print (f"{valor_um:.0f} - {valor_dois:.0f} = {sub:.0f}")
    elif operacao == 3:
        print (f"{valor_um:.0f} x {valor_dois:.0f} = {multi:.0f}")    
    elif operacao == 4:
        print (f"{valor_um:.0f} / {valor_dois:.0f} = {div:.0f}") 

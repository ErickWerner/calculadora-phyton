while True:
    valor = int (input("informe um valor entre 1 e 10: "))
    if 1 <= valor <= 10:
        break
    else:
        print ("Valor inválido")

print (f"Tabuada de valor {valor}:")


for i in range (1,11):
    resultado = valor * i
print (f"{valor} x {i} = {resultado}")
numeros = []

for i in range (10):
    num = int (input("Digite o número {}° ". format (i + 1)))
    numeros.append(num)
numeros.sort()    

print (numeros)    
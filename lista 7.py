contador = 0
soma = 0

for contador in range (1,101):
    if contador % 2 != 1:
        soma += contador
        contador += 1
    if contador == 50:
        break
print ("A soma dos primeiros 50 pares é: ",soma)       
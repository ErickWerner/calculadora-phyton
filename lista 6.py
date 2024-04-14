intervalo = 0
f_intervalo = 0

#recepção dos números
for i in range (10):
    numero = float(input("Digite o {}° número: ". format (i+1)))
    if 10 <= numero <=20:
        intervalo +=1
    else:
        f_intervalo += 1

print (f"{intervalo}números estão dentro do intervalo [10,20]")
print ( f"{f_intervalo} números estão fora do intervalo [10,20]")
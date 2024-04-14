from collections import Counter

lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]

contagem = Counter(lista)

mais_comum = contagem.most_common(1)[0]

print("O número que se repete mais vezes é:", mais_comum[0])

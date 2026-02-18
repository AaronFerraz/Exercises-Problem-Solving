"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valore somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanhoda menor.

Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

resultado:
lista_soma = [2, 4, 6, 8]
"""

from itertools import zip_longest 


lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]
# lista_soma = [i[0] + i[1] for i in zip(lista_a, lista_b)]
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)

lista_soma2 = []

for i in range(len(lista_b) if len(lista_a) >= len(lista_b) else len(lista_a)):
    lista_soma2.append(lista_a[i] + lista_b[i])

print(lista_soma2)


lista_soma3 = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma3)

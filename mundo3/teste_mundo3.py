#tuplas
# tuplas () são imutaveis

lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(type(lanche))
for i in lanche:
    print(i)
print(lanche[:3], f'\n{len(lanche)}')

numeros = (1, 2, 3, 4, 5, 6, 7, 8)
soma = 0
for i in range(0,len(numeros)):
    soma += numeros[i]
print(soma)
print(numeros.index(3))    
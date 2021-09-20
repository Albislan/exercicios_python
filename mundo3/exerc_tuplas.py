from random import randint
a = 'Início'
b = 'Fim'

#os 5 primeiros colocados exercicio 73
#os 4 ultimos da tabela
#uma tupla com os times em ordem alfabetica
#em que posição esta o chapecoense
print(f'{a:*^50}')
times = ('Atletico-MG', 'Palmeiras', 'Flamengo', 'Fortaleza',
        'Bragantino', 'Corinthians', 'Internacional', 'Fluminense',
        'Atletico-PR', 'Cuiaba', 'Atletico-GO', 'Sao Paulo', 'Ceara',
        'Santos', 'Bahia', 'Juventude', 'America', 'Gremio', 'Sport', 'Chapecoense')
print()
primeiros = times[:5]
print(f'Os cincos primeiros colocados são: ', end=' ')
for time in primeiros:
    print(time, end=', ')
print()

print(f'O Chapecoense esta na posição nº {times.index("Chapecoense")+ 1}')            
print(f'{b:*^50}')
#exercicio 74
#gerar 5 numeros aleatorios e guardar numa tupla e 
# mostrar o maior e o menor numero
print(f'{a:*^50}')
numeros = (randint(1,10),)
for n in range(0, 4):
    n = (randint(1,10),)
    numeros += n
print(numeros)
print(numeros.max())
print()
print(f'{b:*^50}')

# criar uma tupla com varios nomes e mostrar as vogais em cada palavra
print(f'{a:*^50}')

print(f'{b:*^50}')

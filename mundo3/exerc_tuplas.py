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
print(f'A Tupla de times da tabela do campeonato brasileiro são: {times}')
print()
primeiros = times[:5]
ultimos = times[16:21] # outra forma times[-4:]
print(f'Os cincos primeiros colocados são: ', end=' ')
for time in primeiros:
    print(time, end=', ')
print()
print(f'Os quatros ultimos colocados são: ', end=' ')
for time in ultimos:
    print(time, end=', ')
print()
print(f'Os times em ordem alfabética {sorted(times)}')
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
print(f' Os numeros sorteados foram {numeros}')
maior = menor = numeros[0] 
for n in numeros:
    if n < menor:
        menor = n
    if n > maior:
        maior = n    

# outra forma bem mais simples, sem utlizar o for
numeros_ordenada = sorted(numeros)

print(f'Na Tupla acima o maior numero é {maior} ou utilizando o \
sorted {numeros_ordenada[-1]} ou ainda utilizando o max {max(numeros)} e \
    o menor é {menor} ou utilizando o min {min(numeros)} ou ainda utilizando\
 sorted {numeros_ordenada[0]}')
print()
print(f'{b:*^50}')

# criar uma tupla com varios nomes e mostrar as vogais em cada palavra
print(f'{a:*^50}')
for palavra in times:
    print('As Vogais (', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=', ')
    print(f') aparecem na palavra {palavra}.')
print()
#  outra forma mais simples 
for palavra in times:
    print(f'\nNa palavra {palavra} temos', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':

            print(letra, end=' ') 

print(f'\n{b:*^50}')

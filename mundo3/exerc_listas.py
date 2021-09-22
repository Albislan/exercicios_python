a = 'Início'
b = 'Fim'
print(f'{a:*^50}')
numeros = []
for n in range(0,5): #exercicio 80
    num = int(input('Digite um valor! \n'))
    if n == 0 or num > numeros[-1]:
        numeros.append(num)
        print('Adicionado ao Final da Lista')
    else:
        i = 0
        while i < len(numeros):
            if num <= numeros[i]:
                numeros.insert(i, num)
                print(f'Adicionado na posição nº {i}')
                break
            i += 1    
print(f' Os valores digitados em ordem são {numeros}')  
print(f'{b:*^50}')  

#o programa vai ler varios numeros e colocá-los numa lista exercicio 81
#quantos numeros foram digitados
#lista ordenada de forma decrescente
#se o valor 5 foi digitado e esta ou não na lista
print()
print(f'{a:*^50}')
numeros2 = list()
continua = 'S'
while True:
    num = int(input('Digite um valor! \n'))
    numeros2.append(num)
    continua =' '
    while continua not in 'SN':
        continua = str(input('Deseja Continuar? [S/N]')).strip().upper()
    if continua == 'N':
        break
print()
print(f' Os numeros digitados foram {numeros2}')
print()
print(f' Foram digitados {len(numeros2)} números')
print()
numeros2.sort(reverse=True)
print(f' Os numeros digitados em ordem decrescente são  {numeros2}')
print()
if 5 not in numeros2:
    print('O numero 5 não esta nesta lista')
else:
    print(F'O numero 5 esta na posição {numeros2.count(5)}')            
print(f'{b:*^50}')

#exercicio 82
#o programa vai ler varios numeros e colocá-los numa lista
#no final exiba 3 listas, uma que foi digitada, outra só com os numeros pares e outra só com os numeros impares
print()
print(f'{a:*^50}')
numeros3 = list()
continua = 'S'
pares = list()
impares = list()
while True:
    num = int(input('Digite um valor! \n'))
    numeros3.append(num)
    continua =' '
    while continua not in 'SN':
        continua = str(input('Deseja Continuar? [S/N]')).strip().upper()
    if continua == 'N':
        break
for num in numeros3:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)       
print()
print(f' A lista completa dos  numeros digitados é  {numeros3}')
print()
print(f' A lista de numeros pares é {pares}')
print()
print(f' A lista de numeros impares é {impares}')
print()            
print(f'{b:*^50}')

#exercicio 83
#crie um programa onde o usuario digita uma expressao qualquer que use parenteses
#o programa deve analisar se a expressão passada esta com os parenteses abertos e fechados na ordem correta
a = 'Início'
b = 'Fim'
# print(f'{a:*^50}')
# numeros = []
# for n in range(0,5): #exercicio 80
#     num = int(input('Digite um valor! \n'))
#     if n == 0 or num > numeros[-1]:
#         numeros.append(num)
#         print('Adicionado ao Final da Lista')
#     else:
#         i = 0
#         while i < len(numeros):
#             if num <= numeros[i]:
#                 numeros.insert(i, num)
#                 print(f'Adicionado na posição nº {i}')
#                 break
#             i += 1    
# print(f' Os valores digitados em ordem são {numeros}')  
# print(f'{b:*^50}')  

# #o programa vai ler varios numeros e colocá-los numa lista exercicio 81
# #quantos numeros foram digitados
# #lista ordenada de forma decrescente
# #se o valor 5 foi digitado e esta ou não na lista
# print()
# print(f'{a:*^50}')
# numeros2 = list()
# continua = 'S'
# while True:
#     num = int(input('Digite um valor! \n'))
#     numeros2.append(num)
#     continua =' '
#     while continua not in 'SN':
#         continua = str(input('Deseja Continuar? [S/N]')).strip().upper()
#     if continua == 'N':
#         break
# print()
# print(f' Os numeros digitados foram {numeros2}')
# print()
# print(f' Foram digitados {len(numeros2)} números')
# print()
# numeros2.sort(reverse=True)
# print(f' Os numeros digitados em ordem decrescente são  {numeros2}')
# print()
# if 5 not in numeros2:
#     print('O numero 5 não esta nesta lista')
# else:
#     print(F'O numero 5 esta na posição {numeros2.count(5)}')            
# print(f'{b:*^50}')

# #exercicio 82
# #o programa vai ler varios numeros e colocá-los numa lista
# #no final exiba 3 listas, uma que foi digitada, outra só com os numeros pares e outra só com os numeros impares
# print()
# print(f'{a:*^50}')
# numeros3 = list()
# continua = 'S'
# pares = list()
# impares = list()
# while True:
#     num = int(input('Digite um valor! \n'))
#     numeros3.append(num)
#     continua =' '
#     while continua not in 'SN':
#         continua = str(input('Deseja Continuar? [S/N]')).strip().upper()
#     if continua == 'N':
#         break
# for num in numeros3:
#     if num % 2 == 0:
#         pares.append(num)
#     else:
#         impares.append(num)       
# print()
# print(f' A lista completa dos  numeros digitados é  {numeros3}')
# print()
# print(f' A lista de numeros pares é {pares}')
# print()
# print(f' A lista de numeros impares é {impares}')
# print()            
# print(f'{b:*^50}')

# #exercicio 83
# #crie um programa onde o usuario digita uma expressao qualquer que use parenteses
# #o programa deve analisar se a expressão passada esta com os parenteses abertos e fechados na ordem correta
# print()
# print(f'{a:*^50}')
# expressao = str(input('Digite a expressao a ser analizada \n'))
# if expressao.count('(') == expressao.count(')'):
#     print('A expressão foi digitada corretamente')
# else:
#     print('Digitado incorretamente')    

# print()
#solução com listas
# pilha = list()
# for simb in expressao:
#     if simb == '(':
#         pilha.append('(')
#     elif simb == ')':
#         if len(pilha) > 0:
#             pilha.pop()
#         else:
#             pilha.append(')')
#             break
# if len(pilha) == 0:
#     print('Sua expressão esta valida')            
# else:
#     print('Sua expressão esta incorreta')
# print(f'{b:*^50}')

#exercicio 84
#crie um programa que leia nome e peso de varias pessoas, guardando tudo em uma lista. No final mostre o seguinte
# print(f'{a:*^50}')
# print()
# pessoas = list()
# continua = 'S'
# while True:
#     pessoa = list()
#     nome = str(input('Digite seu nome: \n'))
#     pessoa.append(nome)
#     peso = float(input('Qual o peso? \n'))
#     pessoa.append(peso)
#     pessoas.append(pessoa[:])
#     pessoa.clear()
#     continua = ' '
#     while continua not in 'SN':
#         continua = str(input('Deseja Continuar? [S/N] ')).strip().upper()
#     if continua == 'N':
#         break    
# #Quantas pessoas foram cadastradas
# print()
# print(f'Foram cadastradas {len(pessoas)} pessoas')
# #uma listagem com as pessoas mais pesadas
# pesadas = list()
# leves = list()
# mais_leve = mais_pesado = pessoas[0][1] 
# print()
# for p in pessoas:
#     if p[1] <= mais_leve:
#         mais_leve = p[1]
#     if p[1] >= mais_pesado:
#         mais_pesado = p[1]
# for p in pessoas:
#     if p[1] == mais_leve:
#         leves.append(p[0])
#     elif p[1] == mais_pesado:
#         pesadas.append(p[0])            
# print(f'Os mais pesado {pesadas} com {mais_pesado} kl \ne os mais leve {leves} com {mais_leve} kl')            
# #uma listagem com as pessoas mais leves
# print()

# print(f'{b:*^50}')

#exercicio 85
#crie um programa onde o usuario possa digitar 7 valores e cadastre-os numa unica ista que mantenha separados os valores pares e impares
#no final mostre os valores pares e impares em ordem crescentes
# print()
# print(f'{a:*^50}')
# print()
# lista_numero = [[], []]
# for i in range(0,7):
#     n = int(input(f'Digite {i+1}º numero \n'))
#     if n % 2 == 0:
#         lista_numero[0].append(n)
#         lista_numero[0].sort()
#     else:
#         lista_numero[1].append(n)
#         lista_numero[1].sort()
# print()
# print(f'Os numeros pares são{lista_numero[0]}. \nOs numeros impares são {lista_numero[1]}.')            
# print(f'{b:*^50}')
#exercicio 86, 87
#crie um programa que cria uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
#mostre no dinal a soma de todos os valores pares digitados
#a soma dos valores da terceira coluna
#o maior valor da segunda linha

print()
print(f'{a:*^50}')
print()
soma_pares = soma_coluna = 0
matriz = [[],[],[]]
for linha in range(0,3):
    for coluna in range(0, 3):
        num = int(input(f'Digite um valor para a posição [{linha}, {coluna}] \n'))
        matriz[linha].append(num)
        if num % 2 == 0:
            soma_pares += num
print()
for linha in matriz:
    print()
    for valor in linha:
        print(f'[{valor:^5}]', end=' ')
for linha in range(0, 3):
    soma_coluna += matriz[linha][2]         
print(f'\nA soma dos valores pares digitados é {soma_pares}')
print(f'A soma da terceira linha é {sum(matriz[2])}')
print(f'A soma da terceira coluna é {soma_coluna}')
print(f'O maior numero da segunda linha é {max(matriz[1])}')
print()    
print(f'{b:*^50}')
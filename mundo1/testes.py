# # import math
# # n = str(input('Digite uma palavra de preferecia "Oi" para testes \n'))
# # print(f' Usando qual é o indice da letra i na frase {n}, o indice é {n.index("i")}\n')
# # print(f' Removendo prefixo que no caso é a letra O da palavra {n}, {n.removeprefix("O")}\n')

# a = 'Início'
# b = 'Fim'
# print(f'{a:*^50}')
# frase = 'Curso em Video Python'
# print(frase.center(70))
# print()
# frase = frase.replace('em', 'de')
# print(frase)
# dividido = frase.split()
# print()
# print(dividido)
# junto = ''
# junto = junto.join(dividido)
# print()
# print(junto)
# print(f'{b:*^50}')
#Strings end
# ######################
#Aritmético begin
# from typing import Collection


# a = 5
# b = 2

# print(f' o valor de {a} ao quadrado é {a**b}\nque é o mesmo que pow(5,2) = {pow(5,2)}') # equivale a 5 ao quadrado
#ordem Precedencia
#1 - ()
#2 - **
#3 - * / // %
#4 - + -
# a = 'Início'
# b = 'Fim'
# print(f'{a:*^50}') #centraliza
# print(f' o valor da conta 3*5+4**2 é {3*5+4**2}')
# print()
# print(f' o valor do calculo 3*(5+4)**2 é {3*(5+4)**2}')
# print()
# print(f'raiz quadrada de 81 é int(81**(1/2)) {int(81**(1/2))}')
# print()
# print(f'raiz cúbica de 127 é int(127**(1/3)) {int(127**(1/3))}')
# print()
# print(f'{a:>20}') # sinal de > alinha a direita, sinal de < alinha a esquerda e o sinal ^ centraliza
# print(f'{(4/3):.2f} é o resultado da divisão de 4/3 com formatação de 2 casas decimais') # formatando 2 casas decimais
# print(f'{b:*^50}')
# Usando a biblioteca math

# num_float = 25.738555454445
# print(math.ceil(num_float)) # arredonda pra cima
# print(math.floor(num_float)) # arredonda pra baixo
# print(math.ceil(math.sqrt(num_float))) # raiz quadrada


#inicializando Condições

#trabalhando com cores
print(f' \033[4;30;47m Meu chapa \033[m')
#30 - Branco, 31 - Vermelho, 32 - Verde, 33 - Amarelo, 34 - Azul, 35 - Roxo, 36 - Verde-azulado, 37 - Cinza
#40 - Branco, 41 - Vermelho, 42 - Verde, 43 - Amarelo, 44 - Azul, 45 - Roxo, 46 - Verde-azulado, 47 - Cinza
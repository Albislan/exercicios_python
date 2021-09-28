#tuplas
# tuplas () são imutaveis

tupla_lanche = ('hamburguer', 'suco', 'pizza', 'pudim')
print(type(tupla_lanche))
for i in tupla_lanche:
    print(i)
print(tupla_lanche[:3], f'\n{len(tupla_lanche)}')

tupla_numeros = (1, 2, 3, 4, 5, 6, 7, 8)
soma_tupla = 0
for i in range(0,len(tupla_numeros)):
    soma_tupla += tupla_numeros[i]
print(soma_tupla)
print(tupla_numeros.index(3))   

lista_lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
#formas de acrescentar em listas
lista_lanche.append('cookie')
lista_lanche.insert(0,'hot dog')
# formas de deletar em listas
# del.lista_lanche[3]
#lista_lanche.pop(3)
#lista_lanche.remove('pudim')
#lista_lache.clear() remove todos itens da lista
#
print(lista_lanche)
valores =list(range(4,11))
print(valores)
#valores.sort() ordena a lista
#valores.sort(reverse=True) ordena em ordem reversa
for i, v in enumerate(valores):
    print(f'no indice {i} consta o valor {v}!') # mostra indice e valores
valores2 = valores[:] # cria uma cópia
print(valores2.index(min(valores2))) # mostra a posicao de indices começando por zero
print(min(valores2))    
print(valores2.count(4)) # mostra a posição do valor começando por 1

dados = list()
dados.append(valores2[:])
print(dados)
dados.append(valores)
print()
print(dados)
for d in dados:
    for v in d:
        print(v)
print(dados[0][4])

#dicionarios
dados_dict = dict()
dados_dict2 = dict()
dados_dict = {'nome': 'Pedro', 'idade': 25}
dados_dict['sexo'] = 'M'
dados_dict['erro'] = 'errou'
del dados_dict['erro'] # sem ponto e parentes - deleta o elemento
print(dados_dict) # dados_dict.clear() limpa todo o dicionario
for k, v in dados_dict.items():
    print(f'a chave "{k}" contem o valor -> "{v}"')
estado = dict()
brasil = list()
for count in range(0, 3):
    estado['uf'] = input('Unidade Federativa\n')
    estado['sigla'] = input('Sigla do estado\n')
    brasil.append(estado.copy())
print(brasil)    
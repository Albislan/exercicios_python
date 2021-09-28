from random import randint
from tqdm import tqdm
import time
from datetime import datetime
from operator import itemgetter, getitem
with tqdm(total=100) as barra_progresso:
    for i in range(10):
        time.sleep(0.2)
        barra_progresso.update(10)
a = 'Início'
b = 'Fim'
#exerccio 90 faça um exercico que receba 1 nome, a media da nota e guarde os dados e a situcao do aluno em um dicionario
# No final mostre o conteudo da estrutura na tela# 
print(f'{a:*^50}')
aluno = dict()
aluno['nome'] = input('Digite seu nome\n')
aluno['media'] = float(input('Qual a sua media de notas\n'))
if aluno['media'] >= 7:
    aluno['situacao'] = 'Aprovado'
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['situacao'] = 'Recuperação'
else:
    aluno['situacao'] = 'Reprovado'    
print()        
for k, v in aluno.items():
    time.sleep(1)
    print(f'A chave "{k}" tem o valor "{v}"')

print(f'{b:*^50}')
# exercicio 91 faca um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios
# Guarde esse resultado em um dicionario. No final coloque o dicionario em ordem, sabendo que o vencedor tirou o maior numero 
print()
print(f'{a:*^50}')
jogo_dado = dict()
nome_vencedor = ''
valor_vencedor = 0
for i in tqdm(range(4)):
    time.sleep(1)
    jogo_dado[f'jogador{i+1}'] = randint(1,6)
print()
ranking = sorted(jogo_dado.items(), key=itemgetter(1), reverse=True) # ordena dicionarios pelo valor e não pela chave
print()
print(f'O vencedor foi o {ranking[0][0]}')
print('*' * 50)
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar ficou o "{v[0]}" com"{v[1]}" pontos')        
print(f'{b:*^50}')
# exercicio 92 faça um programa que leia nome, ano de nascimento e ctps e cadastre-os com a idade num dicionario
# se o ctps for diferente de 0 o dicionario recebera tambem o ano de contratacao e o salario.
# Calcule e acrescente alem da idade, com quantos anos a pessoa vai se aposentar
print()
print(f'{a:*^50}')
dados_func = dict()
while True:
    dados_func['nome'] = input('Qual o nome da pessoa? \n')
    nascimento = int(input('Qual o ano do nascimento?\n'))
    dados_func['idade'] = datetime.now().year - nascimento
    dados_func['ctps'] = int(input('Numero da CTPS, caso não possua digite 0\n'))
    if dados_func['ctps'] == 0:
        break
    ano_contratacao = int(input('Qual o ano de sua contratação? \n'))
    dados_func['ano_contratacao'] = ano_contratacao
    dados_func['salario'] = float(input('Qual o seu salário?\n'))
    dados_func['aposenta_com'] = (ano_contratacao + 35) - nascimento
    break
print()
for k, v in dados_func.items():
    time.sleep(0.2)
    print(f'A chave "{k}" possui o valor "{v}"')
print()
print(f'{b:*^50}')
# exercicio 93  e 95 crie um programa que gerencie o aproveitamento de um jogador de futebol
# o programa vai ler o nome do jogador, quantas partidas ele jogou,depois vai ler a quantidade de gols feitos em cada partida
# no final guarde num dicionario, incluindo o total de gols feitos durante o campeonato
#aprimore o exercicio para que funcione com varios jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
#cada jogador ter um código e mostre o resultado como 2 tabelas a primeira com os dados do jogador, a segunda com a opção de escolher
# qual jogador deseja visualizar o aproveitamento com opção de continuar#
# print()
print(f'{a:*^50}')
ap_jogadores = list()
cod = 1
while True:
    print('*' * 50)
    dados_jogadores = dict()
    dados_jogadores.clear()
    dados_jogadores['cod'] = cod
    dados_jogadores['nome'] = input('Digite o nome do Jogador\n')
    partidas = int(input(f'Digite quantas partidas {dados_jogadores["nome"]} jogou?\n'))
    dados_jogadores['partidas'] = partidas
    gols = list()
    for partida in range(partidas):
        gols.append(int(input(f'Digite o número de gols feitos na {partida+1}ª partida \n')))
    dados_jogadores['gols'] = gols[:]
    dados_jogadores['total_gols'] = sum(gols)
    ap_jogadores.append(dados_jogadores.copy())
    gols.clear()    
    continua = ' '
    while continua not in 'SN':
        continua = input('Deseja Continuar? [S/N]').strip().upper()
    if continua == 'N':
        break
    cod += 1
print('*' * 80)
for i in dados_jogadores.keys():
    print(f'{i:<15}',end='')
print()    
print('*' * 80)
for k, v in enumerate(ap_jogadores):
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()    
print('*' * 80)
while True:
    busca = int(input('Mostrar dados de qual jogador? para parar digite 999\n'))
    if busca == 999:
        break
    elif busca > len(ap_jogadores):
        print(f'"ERRO"  não existe jogador com o código {busca}')
    else:
        print(f' ---Levantamento do jogador {ap_jogadores[busca-1]["nome"]}:')
        for i, g in enumerate(ap_jogadores[busca-1]['gols']):
            print(f' No jogo {i+1} fez {g} gols')
    print('*' * 80)        
print()
print(f'{b:*^50}')
# exercicio 94 crie um programa que leia nome, sexo e idade de varias pessoas, guardando os dados de cada pessoa em um dicionario
# e todos os dicionarios numa lista. No final mostre quantas pessoas foram cadastradas, a média de idade do grupo,
# uma lista com todas as mulheres, e uma lista com todas as pessoas com idade acima da media
# 
print()
print(f'{a:*^50}')
dados_pessoas = list()
soma_idade = 0
while True:
    dados = dict()
    dados['nome'] = input('Digite o nome\n')
    while True:
        dados['sexo'] = input(f'Digite o sexo de {dados["nome"]}[M/F]\n').strip().upper()
        if dados['sexo'] in 'MF':
            break
        print('"ERRO" - Por favor, digite apenas M ou F')
    dados['idade'] = int(input(f'Digite a idade de {dados["nome"]}\n'))
    soma_idade += dados['idade']
    dados_pessoas.append(dados.copy())
    dados.clear()
    continua = ' '
    while continua not in 'SN':
        continua = input('Deseja Continuar? [S/N] ').strip().upper()
    if continua == 'N':
        break
print()
print(f'Foram cadastradas {len(dados_pessoas)} pessoas')
media = soma_idade / len(dados_pessoas)
print(f'A media de idade do grupo é {media:5.2f}')
lista_mulheres = list()
lista_acima_media = list()
for pessoa in dados_pessoas:
    if pessoa['sexo'] == 'F':
        lista_mulheres.append(pessoa['nome'])
    if pessoa['idade'] > media:
        lista_acima_media.append(pessoa['nome'])    
print(f'A lista de Mulheres são {lista_mulheres}')
print(f'A lista de Pessoas com idade acima da média são {lista_acima_media}')        
print()
print(f'{b:*^50}')
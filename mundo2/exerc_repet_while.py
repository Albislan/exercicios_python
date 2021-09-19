a = 'Início'
b = 'Fim'
# ###exercico 70 de compra de produtos na loja
# c = 'loja super baratão'
# print(f'{a:*^50}')
# print('-' * 50)
# print(f'{c.upper():^50}')
# print('-' * 50)
# continua = 'S'
# nome_produto = produto_barato = ''
# total_compra = quant_produtos = menor = cont = 0
# while True:
#     nome_produto = str(input('Nome do Produto: '))
#     preco = float(input('Preço: R$ '))
#     cont += 1
#     total_compra += preco
#     if preco > 1000:
#         quant_produtos += 1
#     if cont == 1 or preco < menor:
#         menor = preco
#         produto_barato = nome_produto       
#     continua = ' '
#     while continua not in 'SN':
#         continua = str(input('Quer Coninuar? [S/N] ')).strip().upper()
#     if continua == 'N':
#         break 
# print()              
# print(f'O Total da compra foi de R$ {total_compra:.2f}')
# print(f'Temos {quant_produtos} produto(s) custando mais de R$ 1.000,00') 
# print(f'O produto mais barato foi {produto_barato} que  custa R$ {menor:.2f}')   
# print(f'{b:*^50}')
#
# #### exercicio 71 do saque no caixa eletronico
d = 'Banco Muitcha Grannna'
print(f'{a:*^50}')
print('-' * 50)
print(f'{d.upper():^50}')
print('-' * 50)
# cedula1 = 1
# cedula5 = 5
# cedula10 = 10
# cedula50 = 50
# resposta = f'Voce sacará '
# saldo_calc = saldo_saque = quant_cedula1 = quant_cedula5 = quant_cedula10 = quant_cedula50 = 0
# valor_digitado = -1
# while valor_digitado <=0:
#     valor_digitado = int(input('Qual o valor voce deseja sacar a partir de R$ 1,00! \n'))
#     saldo_calc = valor_digitado
# while True:
#     if saldo_calc >= cedula50:
#         saldo_saque = saldo_calc % cedula50
#         quant_cedula50 = saldo_calc // cedula50
#         resposta = resposta + f'{quant_cedula50} nota(s) de R$ 50,00'
#         saldo_calc = saldo_saque    
#     elif saldo_calc >= cedula10:
#         if valor_digitado < 50:
#             saldo_saque = saldo_calc % cedula10
#             resposta = resposta + f'{valor_digitado // cedula10} nota(s) de R$ 10,00'
#         else:        
#             saldo_saque = saldo_calc % cedula10
#             quant_cedula10 = saldo_calc // cedula10
#             resposta = resposta + f' e {quant_cedula10} nota(s) de R$ 10,00'
#         saldo_calc = saldo_saque
#     elif saldo_calc >= cedula5:
#         if valor_digitado < 10:
#             saldo_saque = saldo_calc % cedula5
#             resposta = resposta + f'{valor_digitado // cedula5} nota(s) de R$ 5,00'
#         else:        
#             saldo_saque = saldo_calc % cedula5
#             quant_cedula5 = saldo_calc // cedula5
#             resposta = resposta.replace(' e', ',') + f' e {quant_cedula5} nota(s) de R$ 5,00'
#         saldo_calc = saldo_saque
#     elif saldo_calc >= cedula1:
#         if valor_digitado < 5:
#             saldo_saque = saldo_calc % cedula1
#             resposta = resposta + f'{valor_digitado} nota(s) de R$ 1,00'
#         else:    
#             saldo_saque = saldo_calc % cedula1
#             quant_cedula1 = saldo_calc // cedula1
#             resposta = resposta.replace(' e', ',') + f' e {quant_cedula1} nota(s) de R$ 1,00'
#         saldo_calc = saldo_saque        
#     elif saldo_calc == 0:
#         break   
# print()              
# print(resposta)
# #### uma forma mais facil de fazer o exercicio 71 do saque no caixa eletronico
valor = int(input('Que valor voce quer sacar R$ '))
saldo = valor
ced = 200
total_ced = 0
while True:
    if saldo >= ced:
        saldo -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cédula(s) de R$ {ced}')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50    
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1            
        total_ced = 0        
        if saldo == 0:
            break        

print('')
print(f'{b:*^50}')
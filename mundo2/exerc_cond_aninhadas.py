from random import randint
a = 'Início'
b = 'Fim'
produto = 1000.00
print(f'{a:*^50}')
print()
forma_pagto = int(input('Escolha uma opção abaixo que corresponda a forma de pagto.\
    \n"1" - Pagto. "A Vista em Dinheiro"\n"2" - Pagto. "A Vista no cartão"\n"3" - Pagto. "Parcelado em 2x no cartão"\
    \n"4" - Pagto. "Parcelado em 3x ou mais no cartão"\n'))
print()
if forma_pagto == 1:
    print(f'Voce escolheu por pagar "A Vista em Dinheiro", nesse caso voce ira ganhar um desconto de \
        \n10% no valor de seu produto. Seu produto custa R$ {produto:.2f}, mas voce ira pagar apenas \
        \nR$ {produto - (produto * 0.1):.2f}')
elif forma_pagto == 2:
    print(f'Voce escolheu por pagar "A Vista no cartão", nesse caso voce ira ganhar um desconto de \
        \n5% no valor de seu produto. Seu produto custa R$ {produto:.2f}, mas voce ira pagar apenas \
        \nR$ {produto - (produto * 0.05):.2f}')
elif forma_pagto == 3:
    print(f'Voce escolheu por pagar "Parcelado em 2x no cartão", voce ira pagar R$ {produto:.2f}')
elif forma_pagto == 4:
    print(f'Voce escolheu por pagar "Parcelado em 3x ou mais no cartão", nesse caso o produto terá um acrescimo de 20% \
        \nSeu produto custa R$ {produto:.2f}, mas voce ira pagar um total de R$ {produto + (produto * 0.2):.2f}')
else:
    print('Voce escolheu uma opção invalida\nFavor iniciar programa novamente e escolher entre 1 e 4')   
print()     
print(f'{b:*^50}')


print(f'{a:*^50}')
print()
escolha_jogador = int(input('Bem Vindo ao Jogo Jokenpo\nEscolha uma opção:\n"1" - Pedra\n"2" - Tesoura\n"3" - Papel \n'))
escolha_computador = randint(1,3)
print()
if escolha_jogador == 1:
    print('Voce Escolheu Pedra')
    if escolha_computador == 1:
        print('O computador escolheu Pedra também\nDeu Empate')
    elif escolha_computador == 2:
        print('O computador escolheu Tesoura\nVoce ganhou')
    else:
        print('O computador escolheu Papel\nVoce Perdeu')
elif escolha_jogador == 2:
    print('Voce Escolheu Tesoura')
    if escolha_computador == 2:
        print('O computador escolheu Tesoura também\nDeu Empate')
    elif escolha_computador == 1:
        print('O computador escolheu Pedra\nVoce Perdeu')
    else:
        print('O computador escolheu Papel\nVoce Ganhou')
elif escolha_jogador == 3:
    print('Voce Escolheu Papel')
    if escolha_computador == 3:
        print('O computador escolheu Papel também\nDeu Empate')
    elif escolha_computador == 1:
        print('O computador escolheu Pedra\nVoce Ganhou')
    else:
        print('O computador escolheu Tesoura\nVoce Perdeu')
else:
    print('Opção Invalida. Comece o Jogo novamente e escolha entre 1 e 3')                
print()
print(f'{b:*^50}')
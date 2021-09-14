a = 'Início'
b = 'Fim'
print(f'{a:*^50}')
velocidade = int(input('Qual a velocidade do carro:\n'))
if velocidade > 80:
    print(f'Voce excedeu a velocidade permitida e foi multado\nO valor de sua multa é de R$ {float((velocidade - 80) * 7):.2f}')
elif velocidade == 80:
    print('Tome cuidado, voce está no limite da velocidade permitida')
else:
    print('Tenha um bom dia, dirija com segurança')
print(f'{b:*^50}')
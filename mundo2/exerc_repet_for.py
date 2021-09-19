from time import sleep
a = 'Início'
b = 'Fim'
print(f'{a:*^50}')
for i in range(10,-1,-1): # 46
    print(i)
    sleep(1)
print('BUUUMMM KABUMMNM Fogos uhuuuu Ano novo')    
print(f'{b:*^50}')

print(f'{a:*^50}')
for pares in range(1,50):
    if pares % 2 == 0:
        print(pares)
print(f'{b:*^50}')

print(f'{a:*^50}')
soma = 0 # 48
num = 0
for impares in range(1,500):
    if impares % 2 != 0 and impares % 3 == 0:
        soma +=impares
        num += 1
print(f'A soma dos {num} valores são  {soma}')        
print(f'{b:*^50}')

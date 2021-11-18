print ("******* B e m   v i n d o   a o   c u r s o   d e   P y t h o n *******")

print ("Comentários em Python: \# (para uma linha) e \''' (para múltiplas linhas) ")

print ("Entrada e saída, variáveis e tipos primitivos de dados")

print(10)

print(-8.76)

print(False)

print(True)

print('Olá!', 'Meu nome é', 'Rosana')

idade = input('Qual é sua idade?')

print('Minha idade é', idade, 'anos', end='.')

idade = int(idade)

if(idade>=18):
    print('\nTenho',idade, 'anos','Sou maior de idade', sep='-', end='!')
else:
    print('Sou menor de idade')

print()

if(idade>=18):
    print('Sou um eleitor obrigatório')
elif((idade>=16 and idade<18) or idade>=70):
    print('Sou um eleitor facultativo')
else:
    print('Não sou eleitor')




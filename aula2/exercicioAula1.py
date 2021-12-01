# Fazer um algoritmo que calcula o fatorial de um número 'n'

n = int(input("Digite um número: "))
resultado = 1

if(n < 0):
    print('Não existe fatorial de número negativo')
else:
    if(n==0 or n==1):
        pass
    else:
        i=1
        while (i<=n):
            resultado *= i
            i+=1
    print("O fatorial de n é: {}! = {}".format(n,resultado))



# Fazer um algoritmo para verificar se um número 'n' é primo

#n = int(input("Digite um número: "))
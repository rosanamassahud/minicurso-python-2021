#import camelcase

def eh_primo(n):
    if(n<=0):
        print('Número negativo')
    else:
        contador=0
        for i in range(1,n+1):
            if(n%i==0):
                contador +=1
        if(contador==2):
            print('Número primo!')
        else:
            print('Não é primo')        

def fatorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*fatorial(n-1)

def fibonacci(n):
    n_1 = 1
    n_2 = 1
    if(n==1):
        print('fib(1) = 1')
    elif(n==2):
        print('fib(2) = 1, 1')
    elif(n>=3):
        print('fib({}) = 1, 1'.format(n), end='')
        for i in range(3, n+1):
            elem = n_1 + n_2
            print(', {}'.format(elem),end='')
            n_2 = n_1
            n_1 = elem
        print()    



if (__name__ == '__main__'):
    n = int(input("Digite um número: "))
    opcao = int(input("O que deseja fazer? \n\t1-Ver se n é primo\n\t2-Calcular o fatorial de n\n\t3-Gerar a sequência de fibonacci até n\n"))
    if(opcao ==1):
        eh_primo(n)
    elif(opcao==2):
        fat = fatorial(n)
        print('{}! = {}'.format(n,fat))
    elif(opcao==3):
        fibonacci(n)
    else:
        print('Opção inválida!')

    #txt = 'hello world!'
    #c = camelcase.CamelCase()
    #print(c.hump(txt))
# Prova Prática (PP) - Questão 6 Parte 3 

def fatorial(numero: int) -> None:
    while numero < 0 :
        print('Erro! O número não pode ser negativo.')
        numero = int(input('Escolha um número válido: '))

    print(f'{numero}! =', end=' ')
    if numero in [0, 1]:
        print('1')
    else:
        print
        for i in range(numero, 0, -1):
            if i > 1:
                print(i, end=' x ')
            else:
                print(i)

if __name__ == '__main__':
    print('\nEsse programa irá ler um número inteiro positivo e retornará seu fatorial.')
    num = int(input('Escolha um número: '))
    fatorial(num)
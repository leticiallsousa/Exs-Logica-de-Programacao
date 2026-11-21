# Prova Prática (PP) - Questão 6 Parte 2 

import math

def abs(num: float) -> float:
    if num >= 0:
        return num
    return num*-1

if __name__ == '__main__':
    print('\nEsse programa irá ler um número qualquer e retornar seu valor absoluto (em módulo).')
    numero = float(input('Digite um número: '))
    va = abs(numero)
    print('-='*30)
    print(va)

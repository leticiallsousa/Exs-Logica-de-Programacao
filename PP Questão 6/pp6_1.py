# Prova Prática (PP) - Questão 6 Parte 1 (Atrasado)

def soma(n1:float, n2:float) -> float:
    return n1+n2

def subtracao(n1:float, n2:float) -> float:
    return n1-n2

def multiplicacao(n1:float, n2:float) -> float:
    return n1*n2

def divisao(n1:float, n2:float) -> float:
    return n1/n2

if __name__ == '__main__':
    operacao = input('[+] Soma\n[-] Subtração\n[*] Multiplicação\n[/] Divisão\n\nSelecione a operação que deseja realizar: ')
    while operacao not in ['+', '-', '/', '*']:
        operacao = input('Inválido! Escolha entre as opções e tente novamente: ')

    print('\nAgora precisamos escolher os números da operação!\n')

    num1 = float(input('Primeiro número: '))
    num2 = float(input('Segundo número: '))

    if operacao == '+':
        resultado = soma(num1, num2)
    elif operacao == '-':
        resultado = subtracao(num1, num2)
    elif operacao == '*':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/':
        resultado = divisao(num1, num2)

    print(f'O resultado da operação entre os números {num1} e {num2} é igual a {resultado}')


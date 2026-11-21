# Prova Prática (PP) - Questão 6 Parte 4 

'''Elabore a função calcular_notas que recebe um valor inteiro de saque e retorna quantas notas de R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 1 devem ser entregues, usando sempre o menor número possível de notas.'''

def calcular_notas(valor: int):
    valores = [200, 100, 50, 20, 10, 5, 1]
    resultado = ''

    for v in valores:
        resultado += f'R$ {v}: {valor // v}\n'
        valor %= v

    return resultado


if __name__ == '__main__':
    print('\nEsse programa irá receber um valor inteiro de saque e retornar quantas notas devem ser entregues, usando sempre o menor número possível de notas.')

    valor = int(input('Digite o valor do saque: '))
    notas = calcular_notas(valor)
    print(f'Saque concluído! Notas utilizadas:\n{notas}')
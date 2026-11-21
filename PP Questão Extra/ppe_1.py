# Prova Prática (PP) - Questão EXTRA - Manipulação de uma matriz 3 x 5

LINHAS = 3
COLUNAS = 5

matriz = [[0.0] * COLUNAS for _ in range(LINHAS)]

print('Esse programa irá preencher uma matriz 3 x 5 com números reais e mostrar informações sobre ela.')
print('-' * 50)

for i in range(LINHAS):
    for j in range(COLUNAS):
        matriz[i][j] = float(input(f'Digite o valor da posição [{i}][{j}]: '))

print('-' * 50)

print('Exibição na vertical:')
for i in range(LINHAS):
    for j in range(COLUNAS):
        print(f'Linha {i}, Coluna {j}: {matriz[i][j]}')

print('-' * 50)

print('Exibição na horizontal:')
for i in range(LINHAS):
    for j in range(COLUNAS):
        print(matriz[i][j], end=' ')
print()

print('-' * 50)

print('Exibição em formato de tabela:')
for i in range(LINHAS):
    for j in range(COLUNAS):
        print(f'{matriz[i][j]:8.2f}', end=' ')
    print()

print('-' * 50)

soma = 0
maior = matriz[0][0]
menor = matriz[0][0]
maiores_que_10 = 0

for i in range(LINHAS):
    for j in range(COLUNAS):
        valor = matriz[i][j]
        soma += valor

        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor

        if valor > 10:
            maiores_que_10 += 1

media = soma / (LINHAS * COLUNAS)

print(f'Soma dos valores: {soma:.2f}')
print(f'Média dos valores: {media:.2f}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')
print(f'Quantidade de elementos maiores que 10: {maiores_que_10}')
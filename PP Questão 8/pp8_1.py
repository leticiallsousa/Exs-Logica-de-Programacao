# Prova Prática (PP) - Questão 8

numeros = []

while True: 
    num = int(input('Digite um número inteiro: '))
    if num == -1:
        break
    numeros.append(num)

print(f'Lista na horizontal: \n{numeros}\n')
print(f'Lista na vertical:')
for n in numeros:
    print(n, end='\n')
print(f'Quantidade de elementos: {len(numeros)}')
print(f'Soma dos valores: {sum(numeros)}')
print(f'Maior valor: {max(numeros)}')
print(f'Menor valor: {min(numeros)}')

pesquisar = int(input('Pesquise se um número inteiro está na lista: '))
if pesquisar in numeros:
    print(f'O número {pesquisar} está na lista na posição {numeros.index(pesquisar)}!')
else: 
    print(f'O número {pesquisar} não está na lista...')

print(f'Lista na ordem crescente: {sorted(numeros)}')
numeros.insert(1, 33)
print(f'Lista na ordem decrescente: {sorted(numeros, reverse=True)}')

print(f'{(sum(numeros)/len(numeros)):.3f}')

maiores = 0
for n in numeros:
    if n > 10:
        maiores += 1

print(f'Números maiores que 10: {maiores}')
print(f'Porcentagem dos números maiores que 10 na lista: {((maiores/len(numeros))*100):.2f}% dos números')
numeros.remove(33)
print(f'Lista após remover o número 33: {numeros}')

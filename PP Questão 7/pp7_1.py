# Prova Prática (PP) - Questão 7 Parte 1 

numeros = []

while True:
    num = float(input('Digite um número: '))
    if num == -1:
        break

    numeros.append(num)

print(f'Foram digitados um total de {len(numeros)} números.')
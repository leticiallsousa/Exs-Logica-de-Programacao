# Prova Prática (PP) - Questão 7 Parte 3 

generos = []
alturas = []

while True:
    genero = str(input('Digite o seu gênero [M ou F]: '))
    if genero == '-1':
        break
    while genero.upper() not in ['M', 'F']:
        genero = str(input('Inválido! Digite o seu gênero: '))

    generos.append(genero.upper())

    altura = int(input('Digite a sua altura [ex 165]: '))
    while altura < 100 or altura > 220:
        altura = int(input('Inválido! Digite a sua altura: '))

    alturas.append(altura)


print(f'\nRegistro finalizado!\nMaior altura do grupo: {max(alturas)}\nMenor altura do grupo: {min(alturas)}\nQuantidadade de homens: {generos.count('M')}\nQuantidade de mulheres: {generos.count('F')}')

# Prova Prática (PP) - Questão 7 Parte 2 

alunos = []

while True:
    nota = float(input('Digite a nota do aluno: '))
    if nota == -1:
        break

    alunos.append(nota)

print(f'\nRegistro Finalizado.\nQuantidade de alunos: {len(alunos)}\nMédia da turma: {(sum(alunos)/len(alunos)):.2f}')
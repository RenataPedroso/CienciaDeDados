alunos = []
alunos.append({'nome': 'Aluno 01', 'curso': 'Ciências da Computação', 'AV1':8 })
alunos.append({'nome': 'Aluno 02', 'curso': 'Sistemas de Informação', 'AV1':7 })
alunos.append({'nome': 'Aluno 03', 'curso': 'Sistemas de Informação', 'AV1':6 })
alunos.append({'nome': 'Aluno 04', 'curso': 'Sistemas de Informação', 'AV1':6 })
alunos.append({'nome': 'Aluno 05', 'curso': 'Sistemas de Informação', 'AV1':6 })

notas = []
for aluno in alunos:
    notas.append(aluno['AV1'])

print('A MAIOR nota é.....:', max(notas))
print('A MENOR nota é.....:', min(notas))
print('A MÉDIA das notas é: {:.2f}'.format(sum(notas)/len(notas)))
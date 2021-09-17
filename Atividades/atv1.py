#atividade 1 da aula de ciencia de dados

# Dados
alunos = []
alunos.append({'nome': 'Aluno 01', 'curso': 'Ciências da Computação', 'AV1':8 })
alunos.append({'nome': 'Aluno 02', 'curso': 'Sistemas de Informação', 'AV1':7 })
alunos.append({'nome': 'Aluno 03', 'curso': 'Sistemas de Informação', 'AV1':6 })
alunos.append({'nome': 'Aluno 04', 'curso': 'Sistemas de Informação', 'AV1':6 })
alunos.append({'nome': 'Aluno 05', 'curso': 'Sistemas de Informação', 'AV1':6 })
alunos.append({'nome': 'Aluno 06', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1':7 })
alunos.append({'nome': 'Aluno 07', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1':9 })
alunos.append({'nome': 'Aluno 08', 'curso': 'Ciências da Computação', 'AV1':10 })
alunos.append({'nome': 'Aluno 09', 'curso': 'Ciências da Computação', 'AV1':10 })
alunos.append({'nome': 'Aluno 10', 'curso': 'Ciências da Computação', 'AV1':4 })
alunos.append({'nome': 'Aluno 11', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1':5 })
alunos.append({'nome': 'Aluno 11', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1':5 })
alunos.append({'nome': 'Aluno 12', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1':9 })
alunos.append({'nome': 'Aluno 13', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1':9 })
alunos.append({'nome': 'Aluno 14', 'curso': 'Ciências da Computação', 'AV1':7})
alunos.append({'nome': 'Aluno 15', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1':7})
alunos.append({'nome': 'Aluno 16', 'curso': 'Ciências da Computação', 'AV1':6})
alunos.append({'nome': 'Aluno 17', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1':8 })
alunos.append({'nome': 'Aluno 18', 'curso': 'Ciências da Computação', 'AV1':4 })
alunos.append({'nome': 'Aluno 19', 'curso': 'Sistemas de Informação', 'AV1':2 })
alunos.append({'nome': 'Aluno 20', 'curso': 'Análise e Desenvolvimento de Sistemas', 'AV1':9 })

notas = []
for aluno in alunos:
    notas.append(aluno['AV1'])

print('A MAIOR nota é.....:', max(notas))
print('A MENOR nota é.....:', min(notas))
print('A MÉDIA das notas é: {:.2f}'.format(sum(notas)/len(notas)))

cc_notas = []
for aluno in alunos:
  if (aluno['curso'] == 'Ciências da Computação'):
    cc_notas.append(aluno['AV1'])

print('A MAIOR nota é.....:', max(cc_notas))
print('A MENOR nota é.....:', min(cc_notas))
print('A MÉDIA das notas é: {:.1f}'.format(sum(cc_notas)/len(cc_notas)))

ads_notas = []
for aluno in alunos:
  if (aluno['curso'] == 'Análise e Desenvolvimento de Sistemas'):
    ads_notas.append(aluno['AV1'])

print('A MAIOR nota é.....:', max(ads_notas))
print('A MENOR nota é.....:', min(ads_notas))
print('A MÉDIA das notas é: {:.2f}'.format(sum(ads_notas)/len(ads_notas)))

si_notas = []
for aluno in alunos:
  if (aluno['curso'] == 'Sistemas de Informação'):
    si_notas.append(aluno['AV1'])

print('A MAIOR nota é.....:', max(si_notas))
print('A MENOR nota é.....:', min(si_notas))
print('A MÉDIA das notas é: {:.1f}'.format(sum(si_notas)/len(si_notas)))

# resolução 2 - feita por um aluno 
cursos = []
for aluno in alunos:
  if (aluno['curso'] not in cursos):
    cursos.append(aluno['curso'])

cursos.sort()

for curso in cursos:
  notas = [] # uma lista para cada curso
  for aluno in alunos:
    if (aluno['curso'] == curso):
      notas.append(aluno['AV1'])

  print('Curso.........: ', curso)
  print('Notas.........: ', notas)
  print('A maior nota é: ', max(notas))
  print('A menor nota é: ', min(notas))
  print('A média é.....: ', round(sum(notas)/len(notas),2 ) )
  print()

# resolução 3, professor
from collections import defaultdict
dados = defaultdict(list)

[ dados[aluno.get('curso')].append(aluno.get('AV1')) for aluno in alunos]

for curso in dados.items():
  print('Curso.........: ', curso[0])
  print('Notas.........: ', curso[1])
  print('A maior nota é: ', max(curso[1]))
  print('A menor nota é: ', min(curso[1]))
  print('A média é.....: ', round(sum(curso[1])/len(curso[1]),2 ) )
  print()
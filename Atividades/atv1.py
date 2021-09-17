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

# Notas Gerais
# desenvolver aqui o código

notas = []
for aluno in alunos:
    notas.append(aluno['AV1'])

print('A MAIOR nota é.....:', max(notas))
print('A MENOR nota é.....:', min(notas))
print('A MÉDIA das notas é: {:.2f}'.format(sum(notas)/len(notas)))

# Saída
# A MAIOR nota é.....: 10
# A MENOR nota é.....: 2
# A MÉDIA das notas é: 6.86

# Ciências da Computação
# desenvolver aqui o código

cc_notas = []
for aluno in alunos:
  if (aluno['curso'] == 'Ciências da Computação'):
    cc_notas.append(aluno['AV1'])

print('A MAIOR nota é.....:', max(cc_notas))
print('A MENOR nota é.....:', min(cc_notas))
print('A MÉDIA das notas é: {:.1f}'.format(sum(cc_notas)/len(cc_notas)))

# Saída
# A MAIOR nota é.....: 10
# A MENOR nota é.....: 4
# A MÉDIA das notas é: 7.0

# Análise e Desenvolvimento de Sistemas
# desenvolver aqui o código

ads_notas = []
for aluno in alunos:
  if (aluno['curso'] == 'Análise e Desenvolvimento de Sistemas'):
    ads_notas.append(aluno['AV1'])

print('A MAIOR nota é.....:', max(ads_notas))
print('A MENOR nota é.....:', min(ads_notas))
print('A MÉDIA das notas é: {:.2f}'.format(sum(ads_notas)/len(ads_notas)))

# Saída
# A MAIOR nota é.....: 9
# A MENOR nota é.....: 5
# A MÉDIA das notas é: 7.56

si_notas = []
for aluno in alunos:
  if (aluno['curso'] == 'Sistemas de Informação'):
    si_notas.append(aluno['AV1'])

print('A MAIOR nota é.....:', max(si_notas))
print('A MENOR nota é.....:', min(si_notas))
print('A MÉDIA das notas é: {:.1f}'.format(sum(si_notas)/len(si_notas)))

# Saída
# A MAIOR notas é....: 7
# A MENOR nota é.....: 2
# A MÉDIA das notas é: 5.4

#Desenvolva um algoritmo que permita mostrar de uma só vez os resultados do exercício anterior para cada curso.
# Resolução
# desenvolver aqui o código

ads = []
cc = []
si = []

nome = []
nome_duplicados = []

[(ads.append(aluno['AV1']), nome.append(aluno['curso'])) for aluno in alunos if aluno ['curso'] == 'Análise e Desenvolvimento de Sistemas']
[(cc.append(aluno['AV1']), nome.append(aluno['curso'])) for aluno in alunos if aluno ['curso'] == 'Ciências da Computação']
[(si.append(aluno['AV1']), nome.append(aluno['curso'])) for aluno in alunos if aluno ['curso'] == 'Sistemas de Informação']

nome_duplicados = list(set(nome).copy())

print('Curso:' , nome_duplicados[0], ads)
print('A MAIOR nota é.....:', max(ads))
print('A MENOR nota é.....:', min(ads))
print('A MÉDIA das notas é:', round(sum(ads)/len(ads),2))

print('\nCurso:' , nome_duplicados[1], cc)
print('A MAIOR nota é.....:', max(cc))
print('A MENOR nota é.....:', min(cc))
print('A MÉDIA das notas é:', round(sum(cc)/len(cc),2))

print('\nCurso:' , nome_duplicados[2], si)
print('A MAIOR nota é.....:', max(si))
print('A MENOR nota é.....:', min(si))
print('A MÉDIA das notas é:', round(sum(si)/len(si),2))

# Saída
# Curso: Análise e Desenvolvimento de Sistemas [7, 9, 5, 5, 9, 9, 7, 8, 9]
# A MAIOR nota é.....: 9
# A MENOR nota é.....: 5
# A MÉDIA das notas é: 7.56

# Curso: Ciências da Computação [8, 10, 10, 4, 7, 6, 4]
# A MAIOR nota é.....: 10
# A MENOR nota é.....: 4
# A MÉDIA das notas é: 7.0

# Curso: Sistemas de Informação [7, 6, 6, 6, 2]
# A MAIOR nota é.....: 7
# A MENOR nota é.....: 2
# A MÉDIA das notas é: 5.4
"""2) Crie um dicionário que represente as notas de um aluno em diferentes
disciplinas. As chaves devem ser os nomes das disciplinas e os valores devem ser
as notas (use pelo menos 5 disciplinas). Itere sobre o dicionário e imprima cada
par chave-valor. Calcule a média geral do aluno. Delete a Disciplina que estiver
com menor nota.

"""
disciplinas = {'Introdução de Eng.de Soft': 9.0, 'Linguagem de Programação': 10.0, 'Matemática Aplicada': 9.2, 'IHC': 8.9, 'Arquitetura e Org dos Comp': 8.5}

qtd_dis = len(disciplinas) #conta quantidade de itens de um elemento
notas = 0

for materias in disciplinas.keys ( ):
    print(f'Disciplinas: {materias} | Notas: {disciplinas[materias]}') # disciplina é o dicionário, materias é a matéria (iteração)
    notas = notas + disciplinas[materias] # notas += disciplinas[materias] ele vai somar as notas do dicionário  e vai ter que consultar toda vez
    
print ()
media = notas / qtd_dis
print(f"A média geral: {media}")

print ()
menor = min(disciplinas, key = disciplinas.get)
del disciplinas [menor]
for materias in disciplinas.keys ( ):
    print(f'Disciplinas: {materias} | Notas: {disciplinas[materias]}')


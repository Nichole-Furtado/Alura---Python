"""
3) Crie um dicionário que armazene os nomes dos países e seus respectivos
impostos em empresas. Em seguida, imprima o nome dos 5 países com imposto
mais caro do mundo. Imprima as que tiverem imposto maior que 30%. Insira no
dicionário o Paraguai e a sua carga tributária em empresas.

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


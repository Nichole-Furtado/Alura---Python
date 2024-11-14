"""1) Faça um programa que o usuário digite a quantidades de itens que terão no
dicionário, e as suas respectivas chaves e valores, exemplo:
"""

quantidade = int(input("Digite a quantidade de itens do dicionário: "))
dicionario = { }

for qtd_itens in range(quantidade):
    chave = input("Digite a chave:  ")
    valor = input("Digite o valor: ")
    dicionario[chave] = valor
    
print(dicionario)
# Dicionario que é variável sem valor vai ser chave = valor digitado                     


'''
1 - Solicite ao usuário que insira um número e, em seguida, 
use uma estrutura if else para determinar se o número é par ou ímpar.
n = int(input(" Digite um valor: "))

if n  % 2 == 0:
    print("Este número é par!")
else :
    print("Este número é impar!")
'''  
"""
2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos.

idade = int(input(" Digite sua idade: "))

if idade >= 0 and idade <= 12:
    print (" Criança ")
elif idade >= 13 and idade <= 18:
    print("Adolescente")
else:
    print("Adulto")
"""
"""
3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome 
de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.


usuario_correto = "alura"
senha_correta = "alura123"

login = input("Digite o nome do usuário: \n")
senha = int(input("Digite sua senha: \n"))

if usuario == usuario_correto and senha == senha_correta:
    print("Login bem sucedido!")
else:
    print("Credenciais inválidas. Tente novamente.")
    
"""
""""
4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
Terceiro Quadrante: os valores de x e y devem ser menores que zero;
Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
Caso contrário: o ponto está localizado no eixo ou origem.
"""

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x and y > 0:
    print("O ponto está no primeiro quadrante.")
elif x < 0 and y > 0:
    print("O ponto está no segundo quadrante.")
elif x and  y < 0:
    print("O ponto está no terceiro quadrante.")
elif x > 0 and y < 0:
    print("O ponto está no quarto quadrante.")
else:
    print("O ponto está sobre um eixo ou na origem.")
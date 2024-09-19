import os

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")# Pula uma linha, utilizado https://fsymbols.com/pt/letras/
''' OU USAR
print ('"Sabor Express


"") pode quebrar linha dessa forma tbm'''
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

# criar uma função
def finalizar_app():
    os.system('cls') #windows
    #mac os.system('clear')
    print('Finalizando um App\n')
    # serve clear, para limpar a tela e executar o comando
    
#puxar uma informação do usuário

#interpola alguma informação

# colocar dentro de uma função todas as opções
def escolher_opcao():
    opcao = int( input ("Escolha uma opção: "))# Para saber qual ela escolheu, cria uma váriavel, Opcao
    if opcao == 1 :
        print('Cadastrar restaurante')
    elif opcao == 2 :
        print('Listar restaurante')
    elif opcao == 3 :
        print('Ativar restaurante')
    else:
    # print('Finalizar o programa')
        finalizar_app()

#opcao = int( opcao)
# print (opcao == 1)
# print (type(opcao))
# print (type(1))
#print ("Você escolheu a opção", opcao)

#f string ( onde consegue colocar a váriavel dentro da frase)

#print (f"Você escolheu a opção: {opcao}")

"""Utiliza aspas duplas ou só uma"""

def main():
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
if __name__=='__main__':
    main()

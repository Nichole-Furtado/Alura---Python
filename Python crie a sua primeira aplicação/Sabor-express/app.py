import os

#variavel restaurante que é uma lista
restaurantes = []


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

def opcao_invalida():
    print('Opção Inválida\n')
    input('Digite uma tecla para voltar ao menu inicial: ')
    main()

def cadastrar_novo_restaurante ():#Lista
    
    # pass# para quando n completou o código e ele n ficar vermelho, colocar pass

#limpar tela 

    os.system ('cls')
    print ('Cadastro de novos Restaurantes \n')
    nome_do_restaurante = input (' Digite o nome do restaurante que deseja cadastrar : ')
    restaurantes.append(nome_do_restaurante)#append, colocar dentro da lista
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    print('Digite uma tecla para voltar ao menu principal')
    main()# para voltar ao menu inicial
    
        
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
    try:  # após inserir o try precisa realizar  ' CTRL + ]'
        opcao = int( input ("Escolha uma opção: "))# Para saber qual ela escolheu, cria uma váriavel, Opcao
        if opcao == 1 :
            cadastrar_novo_restaurante ()
        elif opcao == 2 :
            print('Listar restaurante')
        elif opcao == 3 :
            print('Ativar restaurante')
        elif opcao == 4:
            finalizar_app()
        else:
        # print('Finalizar o programa')
            opcao_invalida()
    except:
        opcao_invalida()

#except  = 

#opcao = int( opcao)
# print (opcao == 1)
# print (type(opcao))
# print (type(1))
#print ("Você escolheu a opção", opcao)

#f string ( onde consegue colocar a váriavel dentro da frase)

#print (f"Você escolheu a opção: {opcao}")

"""Utiliza aspas duplas ou só uma"""

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__=='__main__':
    main()

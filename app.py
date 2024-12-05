#Importa a Biblioteca 'os' do Python
import os

#FUnção que Exibe o Nome do App
def exibir_nome_do_app():
    print('''
██████╗░███████╗██╗░░░░░██╗██╗░░░██╗███████╗██████╗░  ████████╗██╗░░██╗███████╗
██╔══██╗██╔════╝██║░░░░░██║██║░░░██║██╔════╝██╔══██╗  ╚══██╔══╝██║░░██║██╔════╝
██║░░██║█████╗░░██║░░░░░██║╚██╗░██╔╝█████╗░░██████╔╝  ░░░██║░░░███████║█████╗░░
██║░░██║██╔══╝░░██║░░░░░██║░╚████╔╝░██╔══╝░░██╔══██╗  ░░░██║░░░██╔══██║██╔══╝░░
██████╔╝███████╗███████╗██║░░╚██╔╝░░███████╗██║░░██║  ░░░██║░░░██║░░██║███████╗
╚═════╝░╚══════╝╚══════╝╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝ 

███████╗██╗░░░░░░█████╗░██╗░░░██╗░█████╗░██╗░░░██╗██████╗░
██╔════╝██║░░░░░██╔══██╗██║░░░██║██╔══██╗██║░░░██║██╔══██╗
█████╗░░██║░░░░░███████║╚██╗░██╔╝██║░░██║██║░░░██║██████╔╝
██╔══╝░░██║░░░░░██╔══██║░╚████╔╝░██║░░██║██║░░░██║██╔══██╗
██║░░░░░███████╗██║░░██║░░╚██╔╝░░╚█████╔╝╚██████╔╝██║░░██║
╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░░╚═════╝░╚═╝░░╚═╝\n''')

#Função que Exibe cada uma das Opções
def exibir_opcoes():
    print('(Digite o número referente à opção desejada)')
    print('1. Cadastrar um Restaurante')
    print('2. Listar um Restaurante')
    print('3. Ativar um Restaurante')
    print('0. Sair do Aplicativo\n')

#Função que Finaliza do App
def finalizar_app():
    #Limpa a Interface
    os.system('cls')
    # os.system('clear') no mac
    print('App Finalizado!\n')

#Função que recebe a Opção Desejada pelo Usuário
def escolher_opcao():
    opcao_escolhida = int(input('Digite a Opção Desejada: '))
    # opcao_escolhida = int(opcao_escolhida) Outro modo de fazer

    match (opcao_escolhida):
        case 1:
            print('Cadastrar um Restaurante')
        case 2:
            print('Listar um Restaurante')
        case 3:
            print('Ativar um Restaurante')
        case 0:
            print('Cadastrar Restaurante')
        case _:
            finalizar_app()

    # if (opcao_escolhida == 1):
    #     print('Cadastrar um Restaurante')
    # elif (opcao_escolhida == 2):
    #     print('Listar um Restaurante')
    # elif (opcao_escolhida == 3):
    #     print('Ativar um Restaurante')
    # else:
    #     finalizar_app() 
    # Opção com If, Elif e Else

#Função que define o Comportamento do programa Principal
def main():
    exibir_nome_do_app()
    exibir_opcoes()
    escolher_opcao()

#Executa caso o Programa Principal esteja ativo
if __name__ == '__main__':
    main()

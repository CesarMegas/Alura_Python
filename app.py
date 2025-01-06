#Importa a Biblioteca 'os' do Python
import os

#
restaurantes = ['Pizza', 'Lasanha']

#FUnção que Exibe o Nome do App
def exibir_nome_do_app():
    print('''
░██████╗░██╗░░░░░░░██╗███████╗███████╗████████╗██╗███╗░░██╗  ████████╗░█████╗░░██████╗████████╗██╗░░░██╗
██╔════╝░██║░░██╗░░██║██╔════╝██╔════╝╚══██╔══╝╚█║████╗░██║  ╚══██╔══╝██╔══██╗██╔════╝╚══██╔══╝╚██╗░██╔╝
╚█████╗░░╚██╗████╗██╔╝█████╗░░█████╗░░░░░██║░░░░╚╝██╔██╗██║  ░░░██║░░░███████║╚█████╗░░░░██║░░░░╚████╔╝░
░╚═══██╗░░████╔═████║░██╔══╝░░██╔══╝░░░░░██║░░░░░░██║╚████║  ░░░██║░░░██╔══██║░╚═══██╗░░░██║░░░░░╚██╔╝░░
██████╔╝░░╚██╔╝░╚██╔╝░███████╗███████╗░░░██║░░░░░░██║░╚███║  ░░░██║░░░██║░░██║██████╔╝░░░██║░░░░░░██║░░░
╚═════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░░░╚═╝░░░░░░╚═╝░░╚══╝  ░░░╚═╝░░░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░░░░╚═╝░░░
\n''')

#Função que Exibe cada uma das Opções
def exibir_opcoes():
    print('(Digite o número referente à opção desejada)')
    print('1. Cadastrar um Restaurante')
    print('2. Listar os Restaurantes')
    print('3. Ativar um Restaurante')
    print('0. Sair do Aplicativo\n')

#Função que Finaliza do App
def finalizar_app():
    exibir_subtitulo('App Finalizado!')

#Função que Retorna o Usuário ao Menu Principal do App
def voltar_ao_menu_principal():
    #Exibe um input ao usuário e retorna ao Menu Principal
    input('\nDigite uma tecla para retornar ao Menu Princiapal')
    main()

#Função que é ativada quando o Usuário digitar uma Opção Inválida
def opcao_invalida():
    #Exibe uma mensagem de Opção Inválida e retorna ao Menu Principal
    print('\nOpção Inválida!\n')
    voltar_ao_menu_principal()

#
def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

#Função que Cadastra os Restauranttes na Lista de Restaurantes
def cadastrar_restaurante():

    exibir_subtitulo('Cadastrar um Restaurante')
    #Pede o Nome do Restaurante
    nome_do_restaurante = input('Digite o Nome do Restaurante que deseja cadastrar: ')

    #Adiciona o restaurante na Lista de Restaurantes e retorna ao Menu Principal
    restaurantes.append(nome_do_restaurante)
    print(f'\nO Restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

#Função que Lista todos os Restaurantes presentes na Lista de Restaurantes
def listar_restaurantes():
    exibir_subtitulo('Listar os Restaurantes')

    for restaurante in restaurantes:
        print(f'•{restaurante}')

    voltar_ao_menu_principal()

#Função que recebe a Opção Desejada pelo Usuário
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Digite a Opção Desejada: '))
        # opcao_escolhida = int(opcao_escolhida) Outro modo de fazer
    
        match (opcao_escolhida):
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                print('Ativar um Restaurante')
            case 0:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

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
    os.system('cls')
    exibir_nome_do_app()
    exibir_opcoes()
    escolher_opcao()

#Executa caso o Programa Principal esteja ativo
if __name__ == '__main__':
    main()

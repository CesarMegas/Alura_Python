#Importa a Biblioteca 'os' do Python
import os

#Lista que Armazena os Dicionários que cotém as Informações dos Restaurantes
restaurantes = [{'nome':'Lanche do Palhaço', 'categoria':'Fast Food', 'ativo':False}, 
                {'nome':'Lanche do Churrasco', 'categoria':'Fast Food', 'ativo':True},
                {'nome':'Pizza da Nona', 'categoria':'Italiano', 'ativo':False}]

#Função que Exibe o Nome do App
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
    print('3. Alterar o Estado de um Restaurante')
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

#Função que Exibe os Subtítulos das Opções Selecionadas
def exibir_subtitulo(texto):
    os.system('cls')
    #Cria uma Linha baseada no número de caracteres que receber
    linha = '-' * len(texto)
    #Desenha o Subtítulo
    print(linha)
    print(texto)
    print(linha)
    print()

#Função que Cadastra os Restauranttes na Lista de Restaurantes
def cadastrar_restaurante():

    exibir_subtitulo('Cadastrar um Restaurante')
    #Pede o Nome do Restaurante
    nome_do_restaurante = input('Digite o Nome do Restaurante que deseja cadastrar: ')
    #Pede a Categoria do Restaurante
    categoria_do_restaurante = input(f'\nDigite a Categoria do Restaurante {nome_do_restaurante}: ')

    #Armazena as informações do Restaurante
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False}
    #Adiciona o restaurante na Lista de Restaurantes e retorna ao Menu Principal
    restaurantes.append(dados_do_restaurante)
    print(f'\nO Restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

#Função que Lista todos os Restaurantes presentes na Lista de Restaurantes
def listar_restaurantes():
    exibir_subtitulo('Listar os Restaurantes')

    #Exibe os Títulos das Categorias
    print(f'{'Nomes dos Restaurantes'.ljust(22)} | {'Categorias'.ljust(20)} | Status')
    for restaurante in restaurantes:
        #Pega os vaores de: Nome, Categoria, Ativado(ou não) e os armazena em variáveis
        restaurante_nome = restaurante['nome']
        restaurante_categoria = restaurante['categoria']
        restaurante_ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'

        print(f'• {restaurante_nome.ljust(20)} | {restaurante_categoria.ljust(20)} | {restaurante_ativo.ljust(20)}')

    voltar_ao_menu_principal()

#Função que Altera o Estado de um Restaurante
def alterar_estado_restaurante():
    exibir_subtitulo('Alterar o Estado de um Restaurante')
    #Pede o Nome do Restaurante que deseja Alterar
    nome_do_restaurante = input('Digite o Nome do Restaurante que deseja Alterar o Estado: ')
    #Variável que armazena a condição de Encontrado ou Não Encontrado de um restaurante
    restaurante_encontrado = False
    
    #Laço de repetição que procura o Restaurante na Lista de Restaurantes
    for restaurante in restaurantes:
        #Caso o Restaurante for encontrado
        if nome_do_restaurante == restaurante['nome']:
            #Mostra que o Restaurante foi encontrado
            restaurante_encontrado = True
            #Altera o valor do Restaurante na parte de 'ativo'
            restaurante['ativo'] = not restaurante['ativo']
            #Variável que armazena as mensagens de Ativação e Desativação de um Restaurante
            mensagem = f'\nO Restaurante {nome_do_restaurante} foi Ativado com sucesso!' if restaurante['ativo'] else f'O Restaurante foi Desativado com sucesso!'
            #Exibe a Mensagem
            print(mensagem)

    #Caso o Restaurane não for encontrado
    if not restaurante_encontrado:
        print(f'\nO Restaurante {nome_do_restaurante} não foi encontrado...')

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
                alterar_estado_restaurante()
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

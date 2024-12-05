#Atividade 02 - Módulos e Funções
#Exercício 01 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

numero_digitado = int(input('Digite um número: '))

if (numero_digitado % 2 == 0):
    print(f'O número {numero_digitado} é par!')
else:
    print(f'O número {numero_digitado} é ímpar!')

#Exercício 02 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.

idade_do_usuario = int(input('\nDigite a sua idade: '))

if (0 <= idade_do_usuario <= 12):
    print(f'A idade de {idade_do_usuario} anos está clasiificada como: Criança!')
elif (13 <= idade_do_usuario <= 18):
    print(f'A idade de {idade_do_usuario} anos está clasiificada como: Adolescente!')
elif (19 <= idade_do_usuario):
    print(f'A idade de {idade_do_usuario} anos está clasiificada como: Adulto!')
else:
    print('Opção Inválida!')

#Exercício 03 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

nome_de_usuario = 'user01'
senha = '12345'

nome_de_usuario_digitado = input('\nDigite o Nome de Usuário: ')
senha_digitada = input('Digite a Senha: ')

if ((nome_de_usuario == nome_de_usuario_digitado) and (senha == senha_digitada)):
    print('O Nome de Usuário e a Senha estão Corretos!')
elif ((nome_de_usuario != nome_de_usuario_digitado) and (senha == senha_digitada)):
    print('O Nome de Usuário está Incorreto!')
elif ((nome_de_usuario == nome_de_usuario_digitado) and (senha != senha_digitada)):
    print('A Senha está Incorreta!')
else:
    print('O Nome de Usuário e a Senha estão Incorretos!')

#Exercício 04 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.

coordenada_x = int(input('\nDigite a Coordenada X: '))
coordenada_y = int(input('Digite a Coordenada Y: '))

if ((coordenada_x > 0) and (coordenada_y > 0)):
    print(f'A coordenada ({coordenada_x}, {coordenada_y}) se encontra no Primeiro Quadrante!')
elif ((coordenada_x < 0) and (coordenada_y > 0)):
    print(f'A coordenada ({coordenada_x}, {coordenada_y}) se encontra no Segundo Quadrante!')
elif ((coordenada_x < 0) and (coordenada_y < 0)):
    print(f'A coordenada ({coordenada_x}, {coordenada_y}) se encontra no Terceito Quadrante!')
elif ((coordenada_x > 0) and (coordenada_y < 0)):
    print(f'A coordenada ({coordenada_x}, {coordenada_y}) se encontra no Quarto Quadrante!')
else:
    print(f'A coordenada ({coordenada_x}, {coordenada_y}) se encontra no Eixo ou Origem!')

#Atividade 01 - Manipulação de Strings
#Exercício 01 - Imprima a frase: Python na Escola de Programação da Alura.
print('Python na Escola de Programação da Alura\n')

#Exercício 02 - Imprima a frase: Meu nome é {nome} e tenho {idade} anos em que nome e idade precisam ser valores armazenados em variáveis.
nome = 'César'

idade = 22

print(f'Meu nome é {nome} e tenho {idade} anos.\n')

#Ecercício 03 - Imprima a palavra: ‘ALURA’ de modo que cada letra fique em uma linha, como mostrado a seguir:
#A
#L
#U
#R
#A
print('''A
L
U
R
A\n''')

#Exercício 04 - Imprima a frase: O valor arredondado de pi é: {pi_arredondado} em que o valor de pi precisa ser armazenado em uma variável e arredondado para apenas duas casas decimais. Para facilitar, utilize:
#pi = 3.14159
pi = 3.14159

pi_arredondado = round(pi, 2)

print(f'O valor arredondado de PI é: {pi_arredondado}')

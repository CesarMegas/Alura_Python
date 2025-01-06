# Atividade 03 - Lista, Laços e Exceções
#Exercício 01 - Crie uma lista para cada informação a seguir:

#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['César', 'Luiz', 'Fernando', 'Felipe']
anos = [2002, 2024]

#Exercício 02 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

lista = ['Renan', 'Murilo', 42, 9, 'C']

for elemento in lista:
    print(elemento)

#Exercício 03 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

soma = 0
for numero in range(1, 11, 1):
    if numero % 2 != 0:
        soma += numero

print(f'\n{soma}')

#Exercício 04 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

print()
for numero in range(10, 0, -1):
    print(numero)

#Exercício 05 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

print()
numero_digitado = int(input('Digite um número: '))
print()

for multiplicador in range(1, 11):
    resultado = numero_digitado * multiplicador
    print(f"{numero_digitado} x {multiplicador} = {resultado}")

#Exercício 06 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

lista_numerica = [10, 5, 15, 100]
soma = 0

try:
    for numero in lista_numerica:
        soma += numero
    print(f'\nA soma dos números é: {soma}')
except Exception as e:
    print(f'\nOcorreu um erro: {e}')

#Exercício 07 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista_para_media = []
soma_para_media = 0

try:
    for numero in lista_para_media:
        soma_para_media += numero
    media = soma_para_media / len(lista_para_media)
    print(f'\nA média final é igual a {media}.')
except ZeroDivisionError:
    print('\nA lista está vazia, não é possível calcular a média.')
except Exception as e:
    print(f'\nOcorreu um erro: {e}')

pi_arredondado = round(pi, 2)

print(f'O valor arredondado de PI é: {pi_arredondado}')

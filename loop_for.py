"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

C ou Java

for(int i = 0; i < 10; i++){
    //execução do loop
}

Python
for item in interavel:
    //exercução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    Lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)

# Exemplo de for 1

for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre um lista)

for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)

range(valor_inical, valor_final)
OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

for numero in range(1, 11):
    print(numero)

# Exemplo 4
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

for indice, letra in enumerate(nome):
    print(nome[indice])

for _, letra in enumerate(nome):
    print(nome[letra])

OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline (_)

Exemplo 5
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)

for valor in enumerate(nome):
    print(valor)

Exemplo 6
qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0


for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

Exemplo 7: Para imprimir sem pular linha

nome = 'Geek University'
for letra in nome:
    print(letra, end='')

Tabela de Emoji Unicode: https://apps.timwhitlock.info/emoji/tables/unicode

for num in range(1, 11):
   print('\U0001F60D' * num)

for _ in range(3):
    for num in range(1, 11):
       print('\U0001F60D' * num)
"""
for _ in range(3):
    for num in range(1, 11):
       print('\U0001F60D' * num)




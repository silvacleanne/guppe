"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.
Existem basicamente duas diferenças básicas:
1 - As tuplas são representadas por parênteses ()
2 - As tuplas são imultáveis: Isso significa que so se criar uma tupla ela não muda. Toda opreação em uma tupla gera uma nova tupla.

# Cuidado 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

# Cuidado 2: Tuplas com 1 elemento

tupla3 = (4) # isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # isso é uma tupla
print(tupla4)
print(type(tupla4))

tupla5 = 5, # isso é uma tupla
print(tupla5)
print(type(tupla5))

# Conclusão: Podemos concluir que tuplas são definidas pela vírgula e não pelo uso do parênteses

# Podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla

tupla = ('Geek University', 'Programação em Python: Essencial')

escola, curso = tupla

print(escola)
print(curso)

# OBS: Gerar erro (ValueError) se colocarmos um número diferente de elementos para desenpacotar

# Métodos para adição e remoção de elementos nas tuplas são existente, dado o fato das tuplas serem imutáveis.

# Soma*, Máximo*, Mínimo* e Tamanho

# * Se os elementos forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2) # tuplas são imutáveis
print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)
print(tupla1)
print(tupla2)

tupla1 = tupla1 + tupla2 # tuplas são imutáveis, mas podemos sobrescrever seus valores
print(tupla1)

# Verificar se determinado elemento está contido na tupla

tupla = (1, 2, 3)
print(3 in tupla)
print(4 in tupla)

# Iterando sobre uma tupla

tupla = (1, 2, 3)

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('c'))

escola = tuple('Geek University')
print(escola)
print(escola.count('e'))

# Dicas na utilização de tuplas
# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# O acesso a elementos de uma tupla também é semelhante a de uma lista

print(meses[5])

# Iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# Verificamos em qual indice um elemento está na tupla

print(meses.index('Setembro'))

# OBS: Caso o elemento não exista, será gerado ValueError.

# Dicas na utilização de tuplas
# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

# Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro')

# Slincing

# tupla[inicio:fim:passo]

print(meses[0:])
print(meses[5:])
print(meses[5:9])

# Por quê utilizar tuplas?

# - Tuplas são mais rápido do que listas.
# - Tuplas deixam seu código mais seguro*.

# * Isso porque trabalhar com elementos imutáveis traz segurança para o código.
"""
# Copiando um tupla para outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla # na tupla não temos o problema de Shallow Copy

print(nova)
print(tupla)

outra = (4, 5, 6)

nova = nova + outra
print(nova)
print(tupla)
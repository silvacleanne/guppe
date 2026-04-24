"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais:
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variáveis locais:
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo está
    limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:
nome_de_variavel = nome_de_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que ao declaramos uma variável nós não colocamos
o tipo de dado dela. Este tipo é inferido ao atribuímos o valor à mesma.

Exemplo em C:
int numero = 42

Exemplo em Java:
int numero = 42

"""

numero = 42
print(numero)

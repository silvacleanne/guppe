"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos da Matemática.
- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matamática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
_ Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos, mas não nos importamos com a ordenação deles.
Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados em Python com chave {}

Diferença entre Conjuntos (Set) e Mapas (Dicionários) em Puthon:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;
**************************************************************
# Definindo um conjunto:

# Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos.
print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo será ignorado sem gerar erro e não
# fará parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5, 6, 7, 2, 3}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto

if 13 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

dados = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]

# Listas aceitam valores duplicados, então temos 10 elementos
lista = list(dados)
print(f'Lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = tuple(dados)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionário não aceita valores duplicados, então temos 8 elementos
dicionario = {}.fromkeys(dados, 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

# Conjunto não aceita valores duplicados, então temos 8 elementos
conjunto = set(dados)
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')
*****************************************************************************************
# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34, 22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)
****************************************************************************************
# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes informam
# manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que um uma lista podemos adicionar novos elementos e ter repetição.

cidades = [ 'Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.
# Podemos utilizar o set para isso:

print(len(set(cidades)))
***************************************************************************************
# Adiciondo elementos em um conjunto
s = {1, 2, 3,}

s.add(4)
s.add(4) # Duplicidade não gera erro. Simplemente é ignorado e não é adicionado.
print(s)
*****************************************************************************************
# Remover elementos em um conjunto
s = {1, 2, 3,}
print(s)

# Forma 1

s.remove(3) # NÃO é indice! Informamos o valor a ser remmovido.
print(s)
# OBS: Caso o valor não seja encontrado será gerado o erro KeyError

# Fomra 2

s. discard(2)
s.discard(22) # Se o valor não for encontrado, nenhum erro é gerado
print(s)
********************************************************************************
s = {1, 2, 3,}
print(s)

# Copiando um conjunto para outro... Cria um outro fazendo com que deixe salvo na memória

# Forma 1 - Deep Copy
novo = s.copy()
print(novo)

novo.add(4)
print(novo)
print(s)
********************************************************************************
s = {1, 2, 3,}
print(s)

# Forma 2 - Shallou Copy

novo = s
novo.add(4)
print(novo)
print(s)
*********************************************************************************
s = {1, 2, 3,}
print(s)

# Podemos remover todos os itens de um conjunto
s.clear()
print(s)
**********************************************************************************
# Métodos Matemáticos de Conjuntos
# Imagine que temos dois conjuntos: Um contendo estudantes do curso Python e um contendo estudantes do curso de Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudante_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python também estudam Java.
# Precisamos gerar um conjunto com nome de estudantes únicos.

# Forma 1 - Utilizando union

unico1 = estudantes_python.union(estudante_java)
print(unico1)

# Forma 2 - Utilizando o caractere pipe |
unico2 = estudantes_python | estudante_java
print(unico2)
***********************************************************************************
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudante_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Gerar um conjunto de estudantes que estão em ambos os cursos.

# Forma 1 - Utilizando intersection

ambos1 = estudantes_python.intersection(estudante_java)
print(ambos1)

# Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudante_java
print(ambos2)
*************************************************************************************
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudante_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

so_python = estudantes_python.difference(estudante_java)
print(so_python)

so_java = estudantes_python.difference(estudante_java)
print(so_java)
"""
# Soma*, Máximo*, Mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))

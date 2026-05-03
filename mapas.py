"""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}

# Interar sobre dicionários
receita = {'jan': 100, 'feb': 200, 'mar': 300, 'apr': 400}

for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f' Em {chave} recebi R$ {receita[chave]}')

**********************************************************
receita = {'jan': 100, 'feb': 200, 'mar': 300, 'apr': 400}

print(receita)

# Acessando as chaves
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

receita = {'jan': 100, 'feb': 200, 'mar': 300, 'apr': 400}
print(receita)

# Acessando os valores

print(receita.values())

for valor in receita.values():
    print(valor)
***********************************************************
receita = {'jan': 100, 'feb': 200, 'mar': 300, 'apr': 400}

print(receita)

# Desempacotamento de dicionários

print(receita.items())

for chave, valor in receita.items():
    print(f'chave={chave} valor={valor}')
"""
receita = {'jan': 100, 'feb': 200, 'mar': 300, 'apr': 400}

# Soma*, Máximo*, Mínimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))



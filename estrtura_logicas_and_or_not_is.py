"""
Estrutura Lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not, is
Operadores binários:
    - and, or

Regras de funcionamento:

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se fo False vira True

"""
# 1. Exemplo
ativo = True
logado = False

if ativo or logado:
    print('Bem-vindo usuário!')

# 2. Exemplo
if not ativo:
    print('Você precisa ativar sua conta. Por favor, cheque seu email!')
else:
    print('Bem-vindo usuário!')

# 3. Exemplo
if ativo is True:
    print('Você precisa ativar sua conta. Por favor, cheque seu email!')
else:
    print('Bem-vindo usuário!')



"""
3. Faça um programa que receba três valores e apresenta a soma dos quadrados dos valores lidos.
"""
valor1: int = int(input("Informe um primeiro valor: "))
valor2: int = int(input("Informe um segundo valor: "))
valor3: int = int(input("Informe um terceiro valor: "))

soma: int = int(valor1 * valor1) + (valor2 * valor2) + (valor3 + valor3)

print(f"A soma dos quadrados dos valores {valor1} com {valor2} e {valor3} eh {soma}")
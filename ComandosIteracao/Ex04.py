#EXERCICIO 4 - LISTA COMANDOS DE ITERAÇÃO

M = int(input('1º valor: '))
N = int(input('2º valor: '))
i = M
soma = 0
while i <= N:
    soma = soma + i
    i = i + 1
print(f'Resultado da soma = {soma}')
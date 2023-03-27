#EXERCICIO 4 - LISTA COMANDOS DE ITERAÇÃO

M = int(input('Digite o 1º valor: '))
N = int(input('Digite o 2º valor: '))
soma = 0
i = M

while i <= N:
    soma = soma + i #ACUMULADORA
    i = i + 1       #CONTADOR
print(f'A soma do intervalo é {soma}')

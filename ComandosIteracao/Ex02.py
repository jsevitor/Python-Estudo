#EXERCICIO 2 - LISTA COMANDOS DE ITERAÇÃO

v1 = int(1)
v2 = int(1)
v3 = int(0)
i = int(1)

print(' SEQUENCIA FIBONACCI ')
N = int(input('Quantidade de termos: '))
print('| Valor |', end='')
while i <= N:
    v3 = v1 + v2
    v1 = v2
    v2 = v3
    print(f' {v3} |', end='')
    i = i + 1
print(' ... |')
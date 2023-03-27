#EXERCICIO 2 - LISTA COMANDOS DE ITERAÇÃO

N = int(input('Quantidade de termos: '))
i = 1
v1 = -1
v2 = 1
v3 = 0
print('| Valor |', end='')
while i <= N:
    v3 = v1 + v2
    v1 = v2
    v2 = v3
    print(f' {v3} |', end='')
    i = i + 1


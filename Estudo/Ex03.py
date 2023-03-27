#EXERCICIO 3 - LISTA COMANDOS DE ITERAÇÃO

i = 1
N = 1
while i != 0:
    N = int(input('Digite um numero: '))
    if N == 0 or N < 0:
        i = 0
    else:
        print(f'Quadrado de {N} = {N ** 2}')
        print((f'Cubo de {N} = {N ** 3}'))
        print(f'Raiz Quadrada {N} = {N ** 0.5 :.2f}')

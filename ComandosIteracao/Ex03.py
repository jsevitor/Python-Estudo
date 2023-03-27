#EXERCICIO 3 - LISTA COMANDOS DE ITERAÇÃO
i = int(1)
while not i == 0:
    N = int(input('Digite um valor: '))
    if N == 0:
        i = 0
        print('Finalizado! ')
    else:
        print('=' * 40)
        print(f'Quadrado de {N} = {N ** 2}')
        print(f'Cubo de {N} = {N ** 3}')
        print(f'Raiz Quadrada de {N} = {N ** 0.5:.2f}')
        print('=' * 40)
        i = i + 1

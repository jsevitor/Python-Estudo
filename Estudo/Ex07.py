#EXERCICIO 7 - LISTA COMANDOS DE ITERAÇÃO
i = 1
maior = 0
while i != 0:
    N = int(input('Digite um numero: '))
    if N == 0:
        i = 0
        print('Finalizado!')
    if N > maior:
        maior = N
print()
print(f'O maior do conjunto é {maior}')

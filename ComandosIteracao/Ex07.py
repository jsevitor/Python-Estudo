#EXERCICIO 7 - LISTA COMANDOS DE ITERAÇÃO

i = 1
maior = 0
while i != 0:
    N = int(input('Digite um valor: '))
    if N == 0:
        i = 0
    if N == 1:
        maior = N
    if N > maior:
        maior = N

print(f'Maior valor: {maior}')
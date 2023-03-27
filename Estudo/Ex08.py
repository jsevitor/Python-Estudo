#EXERCICIO 8 - LISTA COMANDOS DE ITERAÇÃO
print('| Valor | Sinal |')
for i in range(1, 101):
    if i % 3 == 0:
        print(f'|   {i}   |   *   |')
    else:
        print(f'|   {i}   |       |')

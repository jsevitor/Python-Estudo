#EXERCICIO 1 - LISTA COMANDOS DE ITERAÇÃO

x = -3
print('|  x  | −x^2 + 4x − 5 | x^2 + 4x + 5 |')
while x <= 3:
    f = ((x ** 2) + (4 * x) - 5)
    g = ((x ** 2) + (4 * x) + 5)
    print(f'|   {x}   |   {f}   |    {g}    |')
    x = x + 0.5

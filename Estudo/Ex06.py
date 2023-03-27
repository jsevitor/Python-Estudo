#EXERCICIO 6 - LISTA COMANDOS DE ITERAÇÃO
i = str('S')
while i != 'N':
    h = float(input('Informe a altura: '))
    sexo = str(input('Informe o sexo [F/M]: '))

    if sexo == 'F':
        peso_ideal = (62.1 * h) - 44.7
    else:
        peso_ideal = (72.7 * h) - 58

    print(f'Seu peso ideal é {peso_ideal :.2f} Kg.')
    print()
    op = str(input('Deseja continuar? [S/N]: '))
    if op == 'N':
        i = 'N'

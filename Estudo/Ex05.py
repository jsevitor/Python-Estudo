#EXERCICIO 5 - LISTA COMANDOS DE ITERAÇÃO

h = float(input('Informe a altura: '))
sexo = str(input('Informe o sexo [F/M]: '))

if sexo == 'F':
    peso_ideal = (62.1 * h) - 44.7
else:
    peso_ideal = (72.7 * h) - 58

print(f'Seu peso ideal é {peso_ideal :.2f} Kg.')


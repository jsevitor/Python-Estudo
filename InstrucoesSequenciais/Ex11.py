#EXERCICIO 11 - LISTA INSTRUÇÕES SEQUENCIAIS

salario = float(input('Informe o salario: '))
finan = float(input('Valor pretendido: '))

if finan <= (salario * 5):
    print('Financiamento Concedido!')
else:
    print('Financiamento Negado!')
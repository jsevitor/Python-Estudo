#EXERCICIO 1 - LISTA DESVIOS CONDICIONAIS

salIncial = float(input('Digite o salario: R$'))
#BONIFICAÇÃO
if salIncial <= 500:
    bon = 0.05
    salBon = salIncial * bon
elif salIncial > 1200:
    bon = 0
    salBon = salIncial * bon
else:
    bon = 0.12
    salBon = salIncial * bon

#AUXILIO ESCOLA
if salIncial <= 600:
    aux = 150
    salNovo = salIncial + salBon + aux
elif salIncial > 600:
    aux = 100
    salNovo = salIncial + salBon + aux

print(f'O funcionario recebeu {int(bon * 100)}% de bonificação')
print(f'O funcionario recebeu R${float(aux)} de auxilio escola')
print(f'O novo salario do funciionario será de R${float(salNovo)}')
#EXERCICIO 8 - LISTA INSTRUÇÕES SEQUENCIAIS
i = int(1)
maior = 0
menor = 0
altF = 0
homens = 0
mulheres = 0

while i <= 3:
    sexo = str(input('Informe o sexo: '))
    altura = float(input("Informe a altura: "))

    if i == 1:
        maior = altura
        menor = altura
    else:
        if altura > maior:
            maior = altura
        if altura < menor:
            menor = altura

    if sexo == 'F':
        altF = altF + altura
        mulheres = mulheres + 1
    else:
        homens = homens + 1

    i = i + 1
media = altF / mulheres
print(f'Maior altura do grupo: {maior} m.')
print(f'Menor altura do grupo: {menor} m.')
print(f'Média altura mulheres: {media} m.')
print(f'Número de homens do grupo: {homens}')




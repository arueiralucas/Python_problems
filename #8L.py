#Calcular o salário líquido 
salario_bruto=float(input('Digite seu salário bruto : '))
horas_extras=float(input('Digite suas horas extras : '))

#Calculando as horas extras considerando 220h por mês
valor_hora_trabalhada=(salario_bruto/220)

#Pegando o Valor do INSS como 8% do salário Bruto
inss=(salario_bruto*0.08)

#Calculo das horas extras
valor_hora_extra=(valor_hora_trabalhada*horas_extras)

#Salário líquido
salario_liquido=((salario_bruto-inss)+valor_hora_extra)

print(f'Seu salário bruto é   : R$ {salario_bruto:.2f} : ')
print(f'Suas horas Extras são : R$ {horas_extras:.2f}  = R$ {valor_hora_trabalhada:.2f} ')
print(f'Seu salário líquido é : R$ {salario_liquido:.2f} ')
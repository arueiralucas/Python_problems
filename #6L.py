#Aumento de Salário
salario_atual= float(input('Qual seu salário atual ?'))
porcenttage_de_aumento=float(input('Qual a porcentaem de aumento : ex 0,2 = 20%  :'  ))
salario_final=((salario_atual*porcenttage_de_aumento)+(salario_atual))
aumento=((salario_atual*porcenttage_de_aumento))
print('Seu salário aumentou {} , e vai ficar {}'.format(aumento,salario_final))
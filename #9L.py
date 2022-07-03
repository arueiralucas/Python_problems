#Conta de Energia
kw = float(input('Digite a quantidade de Quilowatts da conta : '))
conta=kw*0.12
contaf=conta+(conta*0.018)
print(f'O Valor consumido foi de  : {conta:.2f} o Valor a ser pago e de : {contaf:.2f}')
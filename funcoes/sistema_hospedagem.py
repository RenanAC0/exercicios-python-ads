from os import system 
system('cls')

tipo = input('Digite o tipo de hospedagem (S | D | t):')
qt_diarias = int(input('Qual a quantidade de diarias'))

if tipo == 's' or tipo == 'S':
    print(f'Valor total: R$ {qt_diarias * 255.5}')
elif tipo == 'd':
    print(f'Valor total: R$ {qt_diarias * 305.5}')
elif tipo == 't':
    print(f'Valor total: R$ {qt_diarias * 360.5}')
else:
    print(f'Tipo de hospedagem ivalido!!')
    

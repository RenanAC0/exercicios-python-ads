valor = float(input('Digite o valor da compra'))

qt_parcelas = int(input('qual a opçãp de parcelamento 2 | 4 | 6 | 8 |'))

match qt_parcelas:
    case 2: juros = 3
    case 4: juros = 7
    case 6: juros = 9
    case 8: juros = 12
    case _: juros = -1
    
if juros < 0:
    print('opçao inavalida! tente novamente!')
else:
    valor = valor + valor * juros/100
    parcela = valor / qt_parcelas
    print(f'Valor Total R$ {valor:.2f}\n{qt_parcelas} de R$ {parcela:.2f}')

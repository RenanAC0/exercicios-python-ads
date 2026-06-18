placa = input('Digite a sua placa com 8 caracteres: ')

if len(placa) > 8:
    print('Placa inválida')
else:
    digito = int(placa[7])
    Digito = None

    match digito:
        case 1 | 2: Digito = 'Segunda'
        case 3 | 4: Digito = 'Terça'
        case 5 | 6: Digito = 'Quarta'
        case 7 | 8: Digito = 'Quinta'
        case 9 | 0: Digito = 'Sexta-feira'
        case _:
            print('Inválido, tente novamente')

    if Digito:
        print(f'Dia que não pode circular: {Digito}')

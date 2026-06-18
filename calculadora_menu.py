def media(num1, num2):
    return (num1 + num2)/2

def diferença (num1, num2):
    if num1 < num2:
        return num1 - num2
    else:
        return num1 - num2

def produto(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        print('não é possivel dividir por zero')
    else:
        print(f'A divisao é: {num1/num2}')  
        
    

while True:
    print('[1]Média \n [2] Diferença entre o maior e o menor')
    print('[3] produto\[4] Divisão di primeiro numero pelo segundo')
    print('[5] Sair')
    op = int(input('Digite uma Opção'))
    if op == 5: break
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    match op:
        case 1: print(f'A media dos numeros é {media(num1, num2)}')
        case 2: print(f'A diferença entre os números é {produto(num1, num2)}')
        case 3: print(f'O produto entre os números é {diferença(num1, num2)}')
        case 4: divisao(num1,num2)
        case _: print('Opção invalida')
        
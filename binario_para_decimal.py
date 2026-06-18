bin = input('Digite um número binario: ')
n = len(bin) - 1

decimal = 0

for dig in bin:
    decimal = decimal + int(dig)*2**n
    n = n-1 
    
print(f'O binario {bin} equivale ao decimal {decimal}')
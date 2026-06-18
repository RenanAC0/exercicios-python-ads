numero = int(input('Digite um número: '))

for i in range(1, numero + 1):
    match (i % 3 == 0, i % 5 == 0):
        case (True, True):  print('FizzBuzz', end=' ')
        case (True, False): print('Fizz', end=' ')
        case (False, True): print('Buzz', end=' ')
        case _:             print(i, end=' ')

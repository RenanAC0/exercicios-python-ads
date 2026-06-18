def resultado(nota, freq):
    if freq < 75:
        return ' Reprovado por frequencia'
    elif nota < 6: 
        return 'Reprovado por nota.'
    else:
        return 'Aprovado.'
    
nota = float(input('Digite sua nota: '))
freq = int(input('Digite sau frequencia: '))

print(resultado(nota, freq))
    
    

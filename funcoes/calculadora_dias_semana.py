dias_semana=('dom', 'seg', 'ter', 'qua', 'qui', 'sex', 'sab')

hoje = input('Que dia é hoje? ')
qt_dias = int(input('Quantos dias para o evento? '))

evento = (dias_semana.index(hoje) + qt_dias) % 7
print(f'O evento será na {dias_semana[evento]}')

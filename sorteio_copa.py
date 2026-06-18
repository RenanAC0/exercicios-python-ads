from random import shuffle

selecoes = ['Brasil', 'Argentina', 'Chile', 'Bolivia', 'Paraguai', 'França', 'Espanha', 'Portugal']

shuffle(selecoes)

jogos = []

while len(selecoes) > 0:
    time1 = selecoes.pop()
    time2 = selecoes.pop()
    jogos.append((time1, time2))

for i, jogo in enumerate(jogos, start=1):
    print(f'{i}- {jogo[0]} x {jogo[1]}')
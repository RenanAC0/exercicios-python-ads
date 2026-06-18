from subprocess import run

def clear():
    run('clear')

historico = []

def acessar_pagina(pagina):
    historico.append(pagina)
    print(f"Acessando: {pagina}")

def voltar():
    if len(historico) > 1:
        pagina_removida = historico.pop()
        print(f"Voltando da página: {pagina_removida}")
    else:
        print("Não há páginas no histórico.")

def pagina_atual():
    if len(historico) > 0:
        print(f"Página atual: {historico[-1]}")
    else:
        print("Nenhuma página aberta.")

# Execução
acessar_pagina("google.com")
acessar_pagina("youtube.com")
acessar_pagina("github.com")

pagina_atual()

voltar()

pagina_atual()

print(f"Histórico: {historico}")
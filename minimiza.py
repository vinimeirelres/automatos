import automato

def minimizacao(afd):
    estados = afd.estados
    delta = afd.transicoes
    alfabeto = afd.alfabeto
    finais = afd.finais

    estadonovo = "qn"

    #verifica se o automato está fechado, se não estiver, cria um novo estado e aponta onde está nulo para este novo estado
    i = 0
    for estado in estados:
        for simbolo in alfabeto:
            transicao = delta[(estado, simbolo)]

            if i == 0:
                if transicao is not None:
                    continue
                else:
                    estados.append(estadonovo)
                    for simbolo in alfabeto:
                        delta[estadonovo, simbolo] = estadonovo
                    delta[(estado, simbolo)] = estadonovo
                    i = 1
            else:
                if transicao is not None:
                    continue
                    
                else:
                    delta[(estado, simbolo)] = estadonovo


#cria a tabela, com todos os espacos com '' por padrão
    tabelaminimizacao = {}

    for coluna in estados:
        for linha in estados:
            tabelaminimizacao[(coluna, linha)] = ''

#marca metade da tabela com 'x' (um par de estados acontece só uma vez)
    for coluna in estados:
        for linha in estados:

            if coluna == linha:
                tabelaminimizacao[(coluna, linha)] = 'x'
                continue

            if tabelaminimizacao[(linha, coluna)] != 'x':
                tabelaminimizacao[(coluna, linha)] = 'x'

#marca na tabela estados trivialmente não equivalentes (finais e não finais)
    for coluna in estados:
        for linha in estados:
            if tabelaminimizacao[(coluna, linha)] != 'x':
                if (coluna in finais) and (linha not in finais):
                    tabelaminimizacao[(coluna, linha)] = 'x'
    
    print(F"{tabelaminimizacao}")


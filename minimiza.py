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

    #marca metade da tabela com '&' (um par de estados acontece só uma vez)
    for coluna in estados:
        for linha in estados:

            if coluna == linha:
                tabelaminimizacao[(coluna, linha)] = '&'
                continue

            if tabelaminimizacao[(linha, coluna)] != '&':
                tabelaminimizacao[(coluna, linha)] = '&'

    #marca na tabela estados trivialmente não equivalentes (finais e não finais) com 'x'
    for coluna in estados:
        for linha in estados:
            if tabelaminimizacao[(coluna, linha)] == '':
                if (coluna in finais) and (linha not in finais):
                    tabelaminimizacao[(coluna, linha)] = 'x'
                else:
                    if (linha in finais) and (coluna not in finais):
                        tabelaminimizacao[(coluna, linha)] = 'x'



    #função para marcar os estados não equivalentes recursivamente
    def marcar_recursivamente(q1, q2):

        if tabelaminimizacao[(q1,q2)] in ('x', '&'):
            return # se já marcado, sai da recursão

        tabelaminimizacao[(q1,q2)] = 'x' #marca o par atual como não equivalente

        # itera sobre cada simbolo no alfabeto
        for simbolo in alfabeto: 
            # pega o caminho para onde q1, q2 vai
            p1 = delta[(q1, simbolo)]
            p2 = delta[(q2, simbolo)]

            if p1 != p2:
                if tabelaminimizacao[(p1,p2)] == 'x' or tabelaminimizacao[(p2,p1)] == 'x':
                    # se ambos os estados (p1 e p2) existem e são diferentes propaga a não equivalência para os estados alcançados
                    #verifica se ele ou o espelho já são 'x'
                    marcar_recursivamente(p1, p2)
                else:
                    tabelaminimizacao[(p1, p2)] = tabelaminimizacao.get((p1, p2), '') 
                    tabelaminimizacao[(p2, p1)] = tabelaminimizacao.get((p2, p1), '')
        
    #marca na tabela estados não equivalentes
    for coluna in estados:
        for linha in estados: #vê cada registro da tabela
            if tabelaminimizacao[(coluna, linha)] == '':
                for simbolo in alfabeto: #cada simbolo do alfabeto
                    #pega o caminho para onde vai coluna e linha (ex. (q0, q1)-a> (q0, q3), pega (q0, q3))
                    p1 = delta[(coluna, simbolo)]
                    p2 = delta[(linha, simbolo)]

                    if p1 != p2: #verifica se os dois são não são iguais
                       #verifica o caminho na tabela, incluindo espeho
                       if tabelaminimizacao[(p1, p2)] == 'x' or tabelaminimizacao[(p2,p1)] == 'x':
                            #se tiver um 'x' no caminiho, vai para a verificação recursiva
                            marcar_recursivamente(coluna, linha) #verifica recursivamente
                       else:
                            tabelaminimizacao[(p1, p2)] = tabelaminimizacao.get((p1, p2), '') 
    
    #SEGUNDA VERIFICAÇÃO, garante que o primeiro estado verficado seja marcado, caso tenha que ser
    for coluna in estados:
        for linha in estados: #vê cada registro da tabela
            if tabelaminimizacao[(coluna, linha)] == '':
                for simbolo in alfabeto: #cada simbolo do alfabeto
                    #pega o caminho para onde vai coluna e linha (ex. (q0, q1)-a> (q0, q3), pega (q0, q3))
                    p1 = delta[(coluna, simbolo)]
                    p2 = delta[(linha, simbolo)]

                    if p1 != p2: #verifica se os dois são não são iguais
                       #verifica o caminho na tabela, incluindo espeho
                       if tabelaminimizacao[(p1, p2)] == 'x' or tabelaminimizacao[(p2,p1)] == 'x':
                            #se tiver um 'x' no caminiho, vai para a verificação recursiva
                            marcar_recursivamente(coluna, linha) #verifica recursivamente
                       else:
                            tabelaminimizacao[(p1, p2)] = tabelaminimizacao.get((p1, p2), '') 
                            tabelaminimizacao[(p2, p1)] = tabelaminimizacao.get((p2, p1), '')

    estados_minimizados = []

    for coluna in estados:
        for linha in estados:
            if tabelaminimizacao[(coluna, linha)] == '':
                comb = [linha, coluna]
                junta = " ".join(comb)
                estados_minimizados.append(junta)
    


    print(F"{tabelaminimizacao}")




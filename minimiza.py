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
    lista_de_minimizados = []
    mapa_minimizados = {} #cria um mapa de minimizados para conseguir identificar para quais estados apontar no delta
    
    #inicializa o dicionario
    for estado in estados:
        mapa_minimizados[(estado)] = []

    lista_min_finais = []
    lista_min_nfinais = []

    #funciona, mas falta o q0
    for coluna in estados:
        for linha in estados:
            aux = 0
            if tabelaminimizacao[(coluna, linha)] == '':
                if linha in finais:
                    if linha not in lista_min_finais:
                        lista_min_finais.append(linha)
                        aux = 1
                
                if coluna in finais: #agrupa os estados minimizados finais
                    if coluna not in lista_min_finais:
                        lista_min_finais.append(finais)
                        aux = 1

                if aux == 0: #agrupa os estados minimizados não finais
                    if linha not in lista_min_nfinais:
                        lista_min_nfinais.append(linha)
                    if coluna not in lista_min_nfinais:
                        lista_min_nfinais.append(coluna)


                comb = [coluna, linha]
                junta = " ".join(comb)
                estados_minimizados.append(junta)
                

                print(f"{lista_min_finais}\n{lista_min_nfinais}")

                #faz o mapeamento de alternativas para os estados que foram agrupados
                if junta not in mapa_minimizados[(coluna)]: 
                    mapa_minimizados[(coluna)].append(junta)
                if junta not in mapa_minimizados[(linha)]:
                    mapa_minimizados[(linha)].append(junta)


                if coluna not in lista_de_minimizados:
                    lista_de_minimizados.append(coluna) #vê todos os estados linha e coluna que foram agrupados
                if linha not in lista_de_minimizados:
                    lista_de_minimizados.append(linha)

    estados_minimizacao = [afd.inicial]

    #tenta resolver o problema do estado inicial
    for estado in estados_minimizacao:
        for simbolo in alfabeto:
            if delta[(estado, simbolo)] not in lista_de_minimizados and delta[(estado, simbolo)] not in estados_minimizacao:
                estados_minimizacao.append(delta[(estado,simbolo)]) #faz a ponte entre o estado inicial e os estados que foram minimizados, permitindo que seja possivel chegar nele
    
    #adiciona os estados que foram minimizados na lista de estados minimização
    for estado in estados_minimizados:
        estados_minimizacao.append(estado)

    delta_minimizado = {}

    problemas = {}

     #cria o delta do minimizado para os estados que não foram agrupados, coloca a junção em problemas
    for estado in estados_minimizacao:
        for simbolo in alfabeto:
            if estado not in estados_minimizados:
                delta_minimizado[(estado, simbolo)] = delta[(estado,simbolo)]

                if delta[(estado, simbolo)] not in estados_minimizacao:
                    lista_desejada = mapa_minimizados.get((delta[(estado, simbolo)]), [])
                    val = lista_desejada[0]
                    delta_minimizado[(estado, simbolo)] = val

    #adiciona o delta dos estados agrupados, mas sem junção        
    for coluna in estados:
        for linha in estados:
            for simbolo in alfabeto:
                if tabelaminimizacao[(coluna, linha)] == '':
                    p1 = delta[(coluna, simbolo)]
                    p2 = delta[(linha, simbolo)]
#tabulate
                    if p1 == p2:
                        if p1 == linha or p1 == coluna or p2 == linha or p2 == coluna:
                           comb = [coluna, linha]
                           junta = " ".join(comb) #se os dois apontam para um mesmo estado minimizado, ele aponta para ele mesmo

                           combt = [coluna,linha]
                           juntat = " ".join(combt)

                           delta_minimizado[(juntat, simbolo)] = junta
                        else:
                            lista_desejada = mapa_minimizados.get(p1)
                            val = lista_desejada[0]
                            delta_minimizado[(juntat, simbolo)] = val

                    elif tabelaminimizacao[(p1, p2)] == '&':
                        comb = [p2, p1]
                        junta = " ".join(comb)

                        combt = [coluna,linha]
                        juntat = " ".join(combt)

                        delta_minimizado[(juntat, simbolo)] = junta

                    else:
                        comb = [p1, p2]
                        junta = " ".join(comb)

                        combt = [coluna,linha]
                        juntat = " ".join(combt)

                        delta_minimizado[(juntat, simbolo)] = junta

 

    #print(F"{estados_minimizados}\n{delta_minimizado}")



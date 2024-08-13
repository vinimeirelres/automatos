import automato

def minimizacao(afd):
    estados = afd.estados
    delta = afd.transicoes
    alfabeto = afd.alfabeto
    finais = afd.finais

    estadonovo = "qn"

    #verifica se o automato está fechado, se não estiver, cria um novo estado e aponta onde está nulo para este novo estado
    for estado in estados:
        for simbolo in alfabeto:
            transicao = delta[(estado, simbolo)]


            if not transicao:
                delta[(estado, simbolo)] = estadonovo

                if estadonovo not in estados:
                    estados.append(estadonovo)
                    for simbolo in alfabeto:
                        delta[estadonovo, simbolo] = estadonovo

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

    #INICIO DA JUNÇÃO E MAPEAMENTO DOS ESTADOS EQUIVALENTES E CONSTRUÇÃO DO DELTA

    
    estados_minimizados = []
    mapa_minimizados = {} #cria um mapa de minimizados para conseguir identificar para quais estados apontar no delta
    
    #inicializa o dicionario do mapa de estados minimizados
    for estado in estados:
        mapa_minimizados[(estado)] = []

    lista_min_finais = []
    lista_min_nfinais = []

    #fagrupa os estados minimizados finais e não finais nas suas respectovas listas
    for coluna in estados:
        for linha in estados:
            if tabelaminimizacao[(coluna, linha)] == '':

                if linha in finais: #agrupa os estados minimizados finais
                    if linha not in lista_min_finais:
                        lista_min_finais.append(linha)
                
                if coluna in finais: #agrupa os estados minimizados finais
                    if coluna not in lista_min_finais:
                        lista_min_finais.append(coluna)

                if linha not in lista_min_finais: #agrupa os estados minimizados não finais
                    if linha not in lista_min_nfinais:
                        lista_min_nfinais.append(linha)
                
                if coluna not in lista_min_finais: #agrupa os estados minimizados não finais
                    if coluna not in lista_min_nfinais:
                        lista_min_nfinais.append(coluna)
                
    #cria os estados agrupados e cria o mapa de estados minimizados, que mapeia o estado original para um estado agrupado equivalente
    if lista_min_finais:
        finalagrupado = " ".join(lista_min_finais)
        for estado in lista_min_finais: 
            mapa_minimizados[estado].append(finalagrupado)
    else:
        finalagrupado = None
    if lista_min_nfinais:
        nfinalagrupado = " ".join(lista_min_nfinais)
        for estado in lista_min_nfinais: 
            mapa_minimizados[estado].append(nfinalagrupado)
    else:
        nfinalagrupado = None

    
    
    
    #definição do estado
    if afd.inicial in lista_min_nfinais:
        inicial = nfinalagrupado
    else:
        inicial = afd.inicial


    estados_minimizados = [inicial]

    delta_minimizado = {}

    #cria o delta do minimizado para os estados que não foram agrupados
    for estado in estados_minimizados:
        for simbolo in alfabeto:
            if estado is not finalagrupado and estado is not nfinalagrupado:
                delta_minimizado[(estado, simbolo)] = delta[(estado,simbolo)]

                if delta[(estado, simbolo)] not in estados_minimizados:
                    if delta[(estado, simbolo)] in lista_min_finais or delta[(estado, simbolo)] in lista_min_nfinais:
                        lista_desejada = mapa_minimizados.get((delta[(estado, simbolo)]), [])
                        val = lista_desejada[0]
                        delta_minimizado[(estado, simbolo)] = val
                    else:
                        estados_minimizados.append(delta[(estado,simbolo)])

    #adiciona os estados que foram minimizados na lista de estados minimizados
    if inicial is not afd.inicial:
        estados_minimizados.append(finalagrupado)
    else:
        if nfinalagrupado:
            estados_minimizados.append(nfinalagrupado)
        if finalagrupado:
            estados_minimizados.append(finalagrupado)


    if nfinalagrupado:  
        for estado in lista_min_nfinais:         
            for simbolo in alfabeto:
                delta_minimizado[(nfinalagrupado, simbolo)] = None

                p1 = delta[(estado, simbolo)]

                if p1 in lista_min_finais:
                    if finalagrupado is not delta_minimizado[(nfinalagrupado, simbolo)]:
                        delta_minimizado[(nfinalagrupado, simbolo)] = finalagrupado
                elif p1 in lista_min_nfinais:
                    if nfinalagrupado is not delta_minimizado[(nfinalagrupado, simbolo)]:
                        delta_minimizado[(nfinalagrupado, simbolo)] = nfinalagrupado
                elif p1 in estados_minimizados:
                    delta_minimizado[(nfinalagrupado, simbolo)] = p1

    #adiciona o delta dos estados agrupados  
    if finalagrupado:  
        for estado in lista_min_finais:         
            for simbolo in alfabeto:
                delta_minimizado[(finalagrupado, simbolo)] = None
                p1 = delta[(estado, simbolo)]

                if p1 in lista_min_finais:
                    if finalagrupado is not delta_minimizado[(finalagrupado, simbolo)]:
                        delta_minimizado[(finalagrupado, simbolo)] = finalagrupado
                elif p1 in lista_min_nfinais:
                    if nfinalagrupado is not delta_minimizado[(finalagrupado, simbolo)]:
                        delta_minimizado[(finalagrupado, simbolo)] = nfinalagrupado
                elif p1 in estados_minimizados:
                    delta_minimizado[(finalagrupado, simbolo)] = p1
    
    if estadonovo in estados_minimizados:
        estados_minimizados.remove(estadonovo)

        for estado in estados_minimizados:
            for simbolo in alfabeto:
                if delta_minimizado[(estado, simbolo)] == estadonovo:
                    delta_minimizado[(estado, simbolo)] = None

    
    listafinais= [finalagrupado]
#tabulate
    #cria o automato minimizado
    AFDMin = automato.autbase(estados_minimizados, alfabeto, delta_minimizado, inicial, [], listafinais)

    #retorna o automato
    return (AFDMin)
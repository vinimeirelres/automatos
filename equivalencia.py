def equivalencia(afr, afnd):
    """
    Função que verifica se dois autômatos são equivalentes.
    """
    # Se os autômatos têm o mesmo número de estados
    if len(afr.estados) == len(afnd.estados):
        # Se os autômatos têm o mesmo número de estados finais
        if len(afr.estados_finais) == len(afnd.estados_finais):
            # Se os autômatos têm o mesmo número de transições
            if len(afr.transicoes) == len(afnd.transicoes):
                # Se os autômatos têm o mesmo alfabeto
                if afr.alfabeto == afnd.alfabeto:
                    # Se os autômatos têm o mesmo estado inicial
                    if afr.estado_inicial == afnd.estado_inicial:
                        # Se os autômatos têm os mesmos estados finais
                        if afr.estados_finais == afnd.estados_finais:
                            # Se os autômatos têm as mesmas transições
                            if afr.transicoes == afnd.transicoes:
                                    return True
    return False
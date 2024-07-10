import automato

def minimizacao(afd):
    estados = automato.transicoes
    delta = automato.estados
    alfabeto = automato.alfabeto

    estadonovo = 'qn'

    #verifica se o automato está fechado, se não estiver, cria um novo estado e aponta onde está nulo para este novo estado
    for estado in estados:
        i = 0
        for simbolo in alfabeto:
            transicao = delta[(estado, simbolo)]

            if i == 0:
                if transicao != None:
                    continue
                    i = 1
                else:
                    for simbolo in alfabeto:
                        transnovo = [estadonovo, simbolo]
                        delta.extend = transnovo
                    delta[estado, simbolo] = estadonovo
            else:
                if transicao != None:
                    continue
                    
                else:
                    delta[estado, simbolo] = estadonovo


    print(f"\t{estados}\n{delta}\n")
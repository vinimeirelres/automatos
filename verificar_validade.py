def verifica_aceita(automato, palavra):
    estado_atual = [automato.inicial]
    delta = automato.transicoes
    estados = automato.estados
    alfabeto = automato.alfabeto
    palavras_aceitas = automato.conjaceit
    estados_finais = automato.finais
    aceita = 0

    for simbolo in alfabeto:
        for estado in estados:
            if isinstance(delta[(estado, simbolo)], str):
                delta[(estado, simbolo)] = [delta[(estado, simbolo)]]
    print(delta)

    if len(palavra) <= 0:
        return aceita

    if palavra in palavras_aceitas:
        aceita = 1
        return aceita

    i = len(palavra) - 1
    print(i)
    j = 0
    print(j)
    para = 0
    proximo_estado = []
    print(palavra)
    for simbolo in palavra:
        verf = 0
        for estados in estado_atual:
            print(estados)
            proximo_estado_prov = delta[((estados, simbolo))]
            print(proximo_estado_prov)

            if proximo_estado_prov is None:
                continue

            if estados in estados_finais:  # Verifica se é estado atual
                aceita = 1
                print(aceita)
                print("nnnnnnnnn")
                if i == j:  # se estiver no ultimo simbolo e chegar em um estado final a palavra e aceita
                    para = 1
                    break
            else:
                aceita = 0
                print(aceita)
                print("aaaaa")

            if verf == 0:
                proximo_estado = []
                proximo_estado.extend(proximo_estado_prov)
            else:
                proximo_estado.extend(proximo_estado_prov)

            if verf == len(estado_atual) - 1:
                estado_atual = proximo_estado

            verf = verf + 1

            print(proximo_estado)

        if para == 1:
            break
        j = j + 1

    for estado in estado_atual:
        if estado in estados_finais:
            aceita = 1
            break

    print("bbbbb")
    print(estado_atual)
    print(aceita)
    if aceita == 1:
        automato.conjaceit.append(palavra)

    return aceita
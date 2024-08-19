from itertools import combinations
import automato

def afn_to_afd(afn):
    listadecombinacoes = []

    for i in range(1, len(afn.estados)+1): #cria todas as combinacoes possiveis entre os estados, para criacao da tabela de transicao
        listadecombinacoes_aux = list(combinations(afn.estados, i)) #cria todas as combinacoes com 1,2, 3... elementos
        listadecombinacoes.extend(listadecombinacoes_aux)#depois vai concatenando os elementos numa lista de combinacoes completa
    
    delta = afn.transicoes
    alfabeto = afn.alfabeto
    finais = afn.finais
    tabelatransicaoafd = {}
    deltaelemento = []
 
    for combinacao in listadecombinacoes: #faz a tabela de transicao, fazendo a lista de todas as trsnsições de uma combinacao, para todas as combinacoes
        deltacombinacao = []
        for simbolo in alfabeto:#cada combinacao terá o seu delta atrelado com cada um dos simbolos do alfabeto
            i = 0
            for elemento in combinacao:#itera dentro de cada elemento da combinacao para criar o delta da combinacao
                deltaelemento = []
                deltaelemento = delta[(elemento, simbolo)]

                if deltaelemento is None:
                    continue
                elif i == 0:
                    deltacombinacao = deltaelemento[:]#comeca a criar o delta em caso de +1 elememnto, ou define o delta da combinacaoo em caso de 1 elemento
                else:
                    for elemento in deltaelemento:
                        if elemento not in deltacombinacao: #evita que existam elementos repetidos em um delta de combinacao
                            deltacombinacao.extend(deltaelemento) #cria o delta da combinacao concatenando os elementos do delta de cada elemento
                
                i = i+1
            deltacombinacao = " ".join(deltacombinacao)
            aux = " ".join(combinacao)
            tabelatransicaoafd[(aux, simbolo)] = deltacombinacao #salva o delta de cada combinacao, atrelado ao simbolo, criando a tabela de transicao afd



    #------estados finais-------
    estados_finais = []
    for combinacao in listadecombinacoes: #verifica cada uma das combinacoes
        for elemento in combinacao: #procura encontrar um elemento presente nos elementos finais nos elementos das combinacoes
            if elemento in finais:
                if combinacao not in estados_finais: #se ele encontrar e a combinacao nao estiver na lista de estados finais
                    estadofinal = " ".join(combinacao) #junta os elementos da combinacao (ver exemplo um pouco abaixo)
                    estados_finais.append(estadofinal) #e junta cada nova string como um elemento da lista de estados finais

    #-----tabela de transicoes reduzida-------
    auxcomb = []
    for comb in listadecombinacoes: #junta elementos que estao separados nas tuplas em uma so string. ex:(`q0`, `q1`) -> (`q0q1`) em toda a lista
        stringunica = " ".join(comb)
        auxcomb.append(stringunica)

    estados_reduzida = [afn.inicial]
    for estados in auxcomb: #definindo os estados da tabela reduzida
        if estados in tabelatransicaoafd.values():
            if estados not in estados_reduzida:
                estados_reduzida.append(estados)


    def remove_naoacesssiveis(lista_de_estados, inicial, alfabeto, tabelatransicoes): #funcao para remover estados inacessiveis
        acessiveis = []
        for estados in lista_de_estados:  #retira estados inacessiveis que nao foram retirados previamente
            if estados == inicial:
                acessiveis.append(estados)
                continue
            else:
                for estado in lista_de_estados:
                    if estado != estados:
                        for simbolo in alfabeto:
                            if estados == tabelatransicoes[(estado, simbolo)]:
                                if(estados) not in acessiveis:
                                    acessiveis.append(estados)
                                    break
        return acessiveis
    
    #tripla checagem de estados acessiveis
    acessiveisfc = remove_naoacesssiveis(estados_reduzida, afn.inicial, alfabeto, tabelatransicaoafd)
    acessiveisdc = remove_naoacesssiveis(acessiveisfc, afn.inicial, alfabeto, tabelatransicaoafd)
    acessiveistc = remove_naoacesssiveis(acessiveisdc, afn.inicial, alfabeto, tabelatransicaoafd)
    
    estados_reduzida = acessiveistc
    
    finais_reduzida = []
    for estados in estados_reduzida: #definindo os estados finais da tabela reduzida
        if estados in estados_finais:
            finais_reduzida.append(estados)

    #se quiser fazer o indice ser s(i), fazer aqui
    #comparar os estados reduzidos e encontra-los na tabela de transicao
    #substitur os valores da tabela de transicao por s(i) quando eles baterem com os estados reduzidos
    #modificar estados finais, da mesma maneira, para nao haver equivocos
    #modificar estados reduzidos

    tabelareduzidaafd = {}
    i = 0
    for estado in estados_reduzida: #construindo a tabela reduzida
        for simbolo in alfabeto:
            delt = tabelatransicaoafd[(estado, simbolo)]
            delt = "".join(delt)
            tabelareduzidaafd[(estado, simbolo)] = delt #elemento que sera indice vai ter uma so string

    #Contrucao do AFD

    AFD = automato.autbase(estados_reduzida, alfabeto, tabelareduzidaafd, afn.inicial, [], finais_reduzida, 'afd')

    return(AFD)
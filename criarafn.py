import automato

#funcao para criar afn 

def cria_afn():
    
    print("--AFN--\n")
    #-----variaveis locais-------
    estados = input("Digite os estados do AFN: ").split()
    alfabeto = input("\n Informe o alfabeto do AFN: ").split()
    estini = input("\n Informe o estado inicial do AFN: ")
    estfim = input("\n Informe o(s) estado(s) final(s) do AFN: ").split()
    transicoes = {}

    #----definicao do delta do automato------
    print("\nDefina as transições do AFN (delta):\n")

    for estado in estados:
        for simbolo in alfabeto:
            print(f"\t{simbolo}")
            print(f"{estado}\t--------->\t", end="")
            est_prox = input("\n Informe o proximo estado: ").split() #permite que haja mais de uma opcao possivel de caminho para o estado

            #if abaixo trata estados em que o estado nao tiver ligacao com outros por aquele simbolo, coloca-se '0'

            if est_prox == 0: #não há ligacao entre o estado e um proximo por aquele simbolo
                transicoes[(estado, simbolo)] = None
            else:
                transicoes[(estado, simbolo)] = est_prox  #armazenando o automato
    
    #gera o automato, colocando as variaveis locais na classe e salva em uma variavel local
    AFN = automato.autbase(estados, alfabeto, transicoes, estini, [], estfim)   

    #retorna a variavel local
    return(AFN)
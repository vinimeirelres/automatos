import automato

#funcao para criar afd 

def cria_afd():
    
    print("--AFD--\n")
    #-----variaveis locais-------
    estados = input("Digite os estados do AFD: ").split()
    alfabeto = input("\n Informe o alfabeto do AFD: ").split()
    estini = input("\n Informe o estado inicial do AFD: ")
    estfim = input("\n Informe o(s) estado(s) final(s) do AFD: ").split()
    transicoes = {}

    #----definicao do delta do automato------
    print("\nDefina as transições do AFD (delta):\n")

    for estado in estados: #para cada estado
        print(estado)

    for simbolo in alfabeto: #e cada simbolo do alfabeto, ex. q1---a>  e q1---b> caso o alfabeto seja a e b
        print(simbolo)

    for estado in estados:
        for simbolo in alfabeto:
            print(f"\t{simbolo}")
            print(f"{estado}\t--------->\t", end="")
            est_prox = input("\n Informe o proximo estado: ")

            #falta if para tratar casos em que  deixar vazio

            if est_prox == 0: #não há ligacao entre o estado e um proximo por aquele simbolo
                transicoes[(estado, simbolo)] = None
            else:
                transicoes[(estado, simbolo)] = est_prox  #armazenando o automato
    
    #gera o automato, colocando as variaveis locais na classe e salva em uma variavel local
    AFD = automato.autbase(estados, alfabeto, transicoes, estini, [], estfim)   

    #retorna a variavel local
    return(AFD)
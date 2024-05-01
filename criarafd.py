import automato
import sequencias

#funcao para criar afd 

def cria_afd():
    
    print("--AFD--\n")
    estados = input("Digite os estados do AFD: ").split()
    alfabeto = input("\n Informe o alfabeto do AFD: ").split()
    estini = input("\n Informe o estado inicial do AFD: ")
    estfim = input("\n Informe o(s) estado(s) final(s) do AFD: ").split()
    transicoes = {}
    print("\nDefina as transições do AFD (delta):\n")

    for estado in estados:
        print(estado)

    for simbolo in alfabeto:
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
    
    conjunto_aceito = []
    conjunto_aceito = sequencias.gerar_sequencias(estini, "", transicoes, conjunto_aceito, estfim, alfabeto)

    AFD = automato.autbase(estados, alfabeto, transicoes, estini, conjunto_aceito, estfim)   

    return(AFD)
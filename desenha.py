from graphviz import Digraph
import random
import os
#MUDAR
def desenha_automato(aut):
   
    desenho = Digraph() #Definindo que a var desenho é do tipo Digraph()
    desenho.attr(rankdir='LR') #LR siginifica da esquerda para direita. entao o automato será criado usando essa regra
    desenho.attr('node', shape='circle') #definindo os atributos do node (nós)
        
        
    desenho.node('->', shape='none', width='0', heigth='0',label='')
    desenho.edge('->', aut.inicial)
        
    for estado_final in aut.finais: 
        desenho.node(estado_final, shape='doublecircle', fontsize='15', fontcolor='blue')#colocando circulo duplo em todos os estados finais.
    
    for estado in aut.estados:
        for simbolo in aut.alfabeto:
            destinos = aut.transicoes[(estado, simbolo)]
            if destinos: #trata transições vazias (None)
                if isinstance(destinos, list): #se a transição for uma lista, itera sobre a lista e faz várias arestas
                    for destino in destinos:
                        desenho.edge(estado, destino, label=simbolo)
                else:
                    desenho.edge(estado, destinos, label=simbolo)
     #edge insere as setas de acordo com o delta (destinos), label = simbolo siginica que em cima da seta estará o simbolo.
    
    aleatorio = round((random.random())*10,2) #define um numero aleatorio para nome da imagem gerada (cada imagem tera um nome diferente 'aut+numrandom')
    aleatorio = str(aleatorio).replace(".", "")  # converte para string e remove pontos
    
    os.makedirs('imagens', exist_ok = True) #confere se a pasta imagens existe
    caminho = os.path.join('imagens', 'aut' + aleatorio) #cria o caminho para onde o arquivo deve ir, e define o nome do arquivo como aut+aleatorio
    
    res = desenho.render(caminho, format='png',cleanup = True) #gera a imagem e salva em caminho

    if res: #retorno para o usuario da criaçao da imagem
        print(f"Imagem {('aut'+ aleatorio)} gerada com sucesso")
    else:
        print("Erro ao gerar imagem")
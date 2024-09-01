import minimiza
import criarafd
import criarafn
from turing import TuringMachine
import verificar_validade
import converte
import desenha
import equivalencia


#afn = criarafn.cria_afn() #cria o afd e salva na variavel afd

#print(F"\nAlfabeto: {afd.alfabeto}\nEstados: {afd.estados}\nEstado Inicial: {afd.inicial}\nEstado(s) Final(is): {afd.finais}\nTransicoes: {afd.transicoes}\nConjunto Aceitacao: {afd.conjaceit}\n")

#palavra = input("Digite a palavra a ser verificada - AFN").split()

#verpalavra = verificar_validade.verifica_aceita(afn, palavra)
#if verpalavra == 1:
#    print(f"A palavra {palavra} e aceita pelo automato")
#else:
#    print(f"A palavra {palavra} nao e aceita pelo automato")

#print(afn.conjaceit)
afn = criarafn.cria_afn()
desenha.desenha_automato(afn)


print("\n----CONVERSÃO----\n")
afd = converte.afn_to_afd(afn)
desenha.desenha_automato(afd)
#palavra = input("Digite a palavra a ser verificada - AFD").split()


#afd = criarafd.cria_afd()
#desenha.desenha_automato(afd)
#verpalavra = verificar_validade.verifica_aceita(afd, palavra)
#if verpalavra == 1:
#    print(f"A palavra {palavra} e aceita pelo automato")
#else:
#    print(f"A palavra {palavra} nao e aceita pelo automato")

#print("\n")
#afd = converte.afn_to_afd(afn)
#print("\n----MINIMIZAÇÃO----\n")
#minimizado = minimiza.minimizacao(afd)
#desenha.desenha_automato(minimizado)
#print(minimizado.tipo_aut)

#equivalencia = equivalencia.equivalencia(afn, afd)
#if(equivalencia):
  #  print("Os automatos sao equivalentes")
#else:
   # print("Os automatos nao sao equivalentes")

#print(F"\nAlfabeto: {afd.alfabeto}\nEstados: {afd.estados}\nEstado Inicial: {afd.inicial}\nEstado(s) Final(is): {afd.finais}\nTransicoes: {afd.transicoes}\nConjunto Aceitacao: {afd.conjaceit}\n")

fita = " racecar "
inicial = "q0"
estados_aceitacao = {"final"}
transicoes = {
    ("q0", " "): ("q1", " ", "R" ),
    ("q0", "r"): ("q1", "X", "R"),  # Marca 'r' no início com 'X', vai para a direita
    ("q0", "a"): ("q1", "a", "R"),  # Continua para a direita
    ("q0", "c"): ("q1", "c", "R"),  # Continua para a direita
    ("q0", "e"): ("q1", "e", "R"),  # Continua para a direita
    ("q0", "X"): ("q0", "X", "R"),  # Ignora os 'X' e continua

    ("q1", "r"): ("q1", "r", "R"),  # Continua para a direita
    ("q1", "a"): ("q1", "a", "R"),  # Continua para a direita
    ("q1", "c"): ("q1", "c", "R"),  # Continua para a direita
    ("q1", "e"): ("q1", "e", "R"),  # Continua para a direita
    ("q1", "X"): ("q1", "X", "R"),  # Ignora 'X' e continua
    ("q1", " "): ("q2", " ", "L"),  # Ao atingir o fim da fita, move para a esquerda

    ("q2", "r"): ("q3", "r", "L"),  # Se encontrar 'r', substitui por 'X' e retorna ao início
    ("q2", "a"): ("q3", "a", "L"),  # Continua para a esquerda
    ("q2", "c"): ("q3", "c", "L"),  # Continua para a esquerda
    ("q2", "e"): ("q3", "e", "L"),  # Continua para a esquerda
    ("q2", "X"): ("q2", "X", "L"),  # Ignora 'X' e continua para a esquerda

    ("q3", "r"): ("q3", "r", "L"),  # Continua para a esquerda
    ("q3", "a"): ("q3", "a", "L"),  # Continua para a esquerda
    ("q3", "c"): ("q3", "c", "L"),  # Continua para a esquerda
    ("q3", "e"): ("q3", "e", "L"),  # Continua para a esquerda
    ("q3", "X"): ("q0", "X", "R"),  # Ignora 'X' e volta ao início
    ("q3", " "): ("final", " ", "N"),  # Se atingir o início da fita, aceita
}

t = TuringMachine(fita, 
                  inicial=inicial,
                  final=estados_aceitacao,
                  transicoes=transicoes)

res = t.executa()

print("Resultado:\n" + res)
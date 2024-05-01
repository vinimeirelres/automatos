import automato
import criarafd

afd = criarafd.cria_afd()

print(F"\nAlfabeto: {afd.alfabeto}\nEstados: {afd.estados}\nEstado Inicial: {afd.inicial}\nEstado(s) Final(is): {afd.finais}\nTransicoes: {afd.transicoes}\nConjunto Aceitacao: {afd.conjaceit}\n")
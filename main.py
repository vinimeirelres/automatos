import criarafd
import criarafn
import verificar_validade

afn = criarafn.cria_afn() #cria o afd e salva na variavel afd

#print(F"\nAlfabeto: {afd.alfabeto}\nEstados: {afd.estados}\nEstado Inicial: {afd.inicial}\nEstado(s) Final(is): {afd.finais}\nTransicoes: {afd.transicoes}\nConjunto Aceitacao: {afd.conjaceit}\n")

palavra = input("Digite a palavra a ser verificada - AFN").split()

verpalavra = verificar_validade.verifica_aceita(afn, palavra)
if verpalavra == 1:
    print(f"A palavra {palavra} e aceita pelo automato")
else:
    print(f"A palavra {palavra} nao e aceita pelo automato")

print(afn.conjaceit)

afd = criarafd.cria_afd()
palavra = input("Digite a palavra a ser verificada - AFD").split()

verpalavra = verificar_validade.verifica_aceita(afd, palavra)
if verpalavra == 1:
    print(f"A palavra {palavra} e aceita pelo automato")
else:
    print(f"A palavra {palavra} nao e aceita pelo automato")

print(afd.conjaceit)



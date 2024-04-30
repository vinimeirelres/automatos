import automato

automato.autbase.alfabeto = input("Digite o alfabeto do automato")
automato.autbase.conjuntoaceitacao = input("Digite o conjunto aceitacao do automato")
automato.autbase.estados = input("Digite os estados do automato")
automato.autbase.inicial = input("Digite o estado inicial do automato")
automato.autbase.transicoes = input("Digite as transicoes do automato")

print(automato.autbase.transicoes, automato.autbase.alfabeto, automato.autbase.conjuntoaceitacao, automato.autbase.estados, automato.autbase.inicial)
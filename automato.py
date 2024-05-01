#classe genérica base para automato

class autbase:

    def __init__(self, estados, alfabeto, transicoes, inicial, conjaceit, finais):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.inicial = inicial
        self.conjaceit = conjaceit 
        self.finais = finais
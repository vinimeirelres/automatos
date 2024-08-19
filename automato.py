#classe genérica base para automato

class autbase:

    def __init__(self, estados, alfabeto, transicoes, inicial, conjaceit, finais, tipo_aut):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transicoes = transicoes
        self.inicial = inicial
        self.conjaceit = conjaceit 
        self.finais = finais
        self.tipo_aut = tipo_aut
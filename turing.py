class TuringMachine(object):
    blank_symbol = "*"

    def __init__(self, fita="", blank_symbol=" ", inicial="", final=None, transicoes=None):
        self.fita = dict(enumerate(fita))
        blank_symbol = blank_symbol
        self.inicial = inicial
        if final == None:
            self.final = set()
        else:
            self.final = set(final)

        if transicoes == None:
            self.transicoes = {}
        else:
            self.transicoes = transicoes
        self.posicao_cabecote = 0
        self.atual = inicial

    def leitura(self):
        posicao_lendo = self.fita[self.posicao_cabecote]
        x = (self.atual, posicao_lendo)
        if x in self.transicoes:
            y = self.transicoes[x]
            self.fita[self.posicao_cabecote] = y[1]
            if y[2] == "R":
                self.posicao_cabecote += 1
            elif y[2] == "L":
                self.posicao_cabecote -= 1
            self.atual = y[0]

    def verfinal(self):
        if self.atual in self.final:
            return True
        else:
            return False
        
    def return_fita(self):
        ft = ""
    
        tamanho = len(self.fita)-1

        for i in range(0, tamanho):
            ft += self.fita[i]

        return ft
    
    def executa(self):
        while not self.verfinal():
            self.leitura()
        
        return self.return_fita()
import minimiza
import converte
import desenha

def equivalencia(aut1, aut2):

    if (aut1.tipo_aut == 'afd' and aut2.tipo_aut == 'afd'):

        aut1_min = minimiza.minimizacao(aut1)
        aut2_min = minimiza.minimizacao(aut2)

        if len(aut1_min.estados) != len(aut2_min.estados):
            return False
        
        if set(aut1_min.finais) != set(aut2_min.finais):
            return False
        
        if aut1_min.transicoes != aut2_min.transicoes:
            return False
        
        if aut1_min.alfabeto != aut2_min.alfabeto:
            return False
        
        if aut1_min.inicial != aut2_min.inicial:
            return False
        
        return True
    else:
        if(aut1.tipo_aut == 'afn'):
            aut1 = converte.afn_to_afd(aut1)
        if(aut2.tipo_aut == 'afn'):
            aut2 = converte.afn_to_afd(aut2)

    
        aut1_min = minimiza.minimizacao(aut1)
        aut2_min = minimiza.minimizacao(aut2)


        if len(aut1_min.estados) != len(aut2_min.estados):
            return False
        
        if set(aut1_min.finais) != set(aut2_min.finais):
            return False
        
        if aut1_min.transicoes != aut2_min.transicoes:
            return False
        
        if aut1_min.alfabeto != aut2_min.alfabeto:
            return False
        
        if aut1_min.inicial != aut2_min.inicial:
            return False
        
        return True

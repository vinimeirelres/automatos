def verifica_aceita(automato, palavra):
  
  estado_atual = [automato.inicial]
  delta = automato.transicoes
  palavras_aceitas = automato.conjaceit
  estados_finais = automato.finais
  aceita = 0
  
  if(len(palavra)) <= 0:
    return (aceita)

  if palavra in palavras_aceitas:
    aceita = 1
    return (aceita)
  

  i = len(palavra)-1
  j = 0
  para = 0
  proximo_estado = []

  for simbolo in palavra:
    verf = 0
    for estados in estado_atual:
      proximo_estado_prov = delta.get((estados, simbolo))

      print(estados)
      if estados in estados_finais:  # Verifica se é estado atual
        aceita = 1
        if i == j: #se estiver no ultimo simbolo e chegar em um estado final a palavra e aceita
          para = 1
          break
      else:
        aceita = 0


      if verf == 0:
        proximo_estado = []
        proximo_estado.append(proximo_estado_prov)
      else:
        proximo_estado.append(proximo_estado_prov)

      if verf == len(estado_atual)-1:
        estado_atual = proximo_estado
      
      verf = verf+1

    if para == 1:
      break
    j = j+1
    print(aceita)

  if aceita == 1:
    automato.conjaceit.append(palavra)

  return (aceita) 
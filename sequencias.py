def gerar_sequencias(estado_atual, palavra, delta, palavras_aceitas, estados_finais, alfabeto):

  if estado_atual in estados_finais and len(palavra) >= 1:  # Verifica se é palavra válida
    palavras_aceitas.append(palavra)
    print(f"Palavra reconhecida: {palavra}")

  for simbolo in alfabeto:  # Para cada símbolo do alfabeto
    proximo_estado = delta.get((estado_atual, simbolo))
    nova_palavra = palavra + simbolo
    gerar_sequencias(proximo_estado, nova_palavra, delta, palavras_aceitas, estados_finais, alfabeto)


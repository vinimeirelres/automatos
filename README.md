# Automatos

Este projeto oferece uma interface web construída com **Flask** para criar e manipular autômatos.
As principais funcionalidades incluem:

- Criação de autômatos finitos determinísticos (AFD) e não determinísticos (AFN);
- Conversão de AFN para AFD;
- Minimização de AFD;
- Geração de imagens dos autômatos criados;
- Verificação de equivalência entre autômatos;
- Validação de palavras em relação a um autômato;
- Testes com máquina de Turing.

---

## Autores

- Júlia Marques Boaventura 
- Vinícius Meireles Pereira Santos

---


## Instalação

1. Instale o **Python 3** a partir de [python.org](https://www.python.org/downloads/).
2. Instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```
3. Instale o software **Graphviz** disponível em [graphviz.org](https://graphviz.org/download/).
   - Após a instalação, adicione o caminho da pasta `bin` do Graphviz à variável de ambiente `PATH` do sistema.

## Executando a aplicação

Com as dependências instaladas e o Graphviz configurado, execute:

```bash
python routes.py
```

Acesse `http://localhost:5000` no navegador para utilizar a interface.

### Opções da interface

Na página inicial são disponibilizadas as seguintes ações:

1. **AFD** – criar um autômato finito determinístico;
2. **AFN** – criar um autômato finito não determinístico;
3. **Máquina de Turing** – testar uma máquina de Turing definida pelo usuário;
4. **Converter AFD para AFN** – converter um AFN salvo para AFD;
5. **Minimizar AFD** – minimizar um AFD existente;
6. **Gerar Imagem de um Autômato** – visualizar graficamente um autômato salvo;
7. **Verificar Validade da Palavra** – conferir se uma palavra é aceita por um autômato;
8. **Verificar Equivalência entre Autômatos** – comparar dois autômatos.

## Estrutura de diretórios

- `afds/` – armazena os AFDs criados em formato `.pkl`;
- `afns/` – armazena os AFNs criados em formato `.pkl`;
- `static/` – arquivos estáticos (CSS e imagens geradas). As imagens ficam em `static/imagens/`;
- `templates/` – templates HTML utilizados pelo Flask.

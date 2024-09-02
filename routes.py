from turing import TuringMachine
import equivalencia
import verificar_validade
import minimiza
from automato import autbase
import desenha
import converte
import os
import pickle
from flask import Flask, render_template, request,redirect, url_for

app = Flask(__name__, static_url_path='/static')

os.makedirs('afds', exist_ok = True) 
os.makedirs('afns', exist_ok = True) 


def lista_arquivos(diretorio):
    itens = os.listdir(diretorio)
    arquivos = [item for item in itens if item.endswith('.pkl')]
    return arquivos

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/afd', methods=['GET'])
def afd():
    return render_template('afd.html')

@app.route('/afn', methods=['GET'])
def afn():
    return render_template('afn.html')

@app.route('/redturing', methods=['GET'])
def redturing():
    return render_template('turing.html')

@app.route('/converter', methods=['GET'])
def converter():
    diretorio = 'afns'
    afns = lista_arquivos(diretorio)
    return render_template('converter.html', arquivos = afns)

@app.route('/minimiza', methods=['GET'])
def minimizar():
    diretorio = 'afds'
    afds = lista_arquivos(diretorio)
    return render_template('minimizar.html', arquivos = afds)

@app.route('/geraimagem', methods=['GET'])
def gimagem():
    diretorio1 = 'afds'
    diretorio2 = 'afns'  
    afds = lista_arquivos(diretorio1)
    afns = lista_arquivos(diretorio2)

    todos_aut = [(diretorio1, f) for f in afds] + [(diretorio2, f) for f in afns]

    return render_template('geraimagem.html', arquivos=todos_aut)

@app.route('/equivalencia', methods=['GET'])
def equivale():
    diretorio1 = 'afds'
    diretorio2 = 'afns'  
    afds = lista_arquivos(diretorio1)
    afns = lista_arquivos(diretorio2)

    todos_aut = [(diretorio1, f) for f in afds] + [(diretorio2, f) for f in afns]

    return render_template('equivalencia.html', arquivos=todos_aut)

@app.route('/verpalavra', methods=['GET'])
def vepalavra():
    diretorio1 = 'afds'
    diretorio2 = 'afns'  
    afds = lista_arquivos(diretorio1)
    afns = lista_arquivos(diretorio2)

    todos_aut = [(diretorio1, f) for f in afds] + [(diretorio2, f) for f in afns]

    return render_template('verificapalavra.html', arquivos = todos_aut)

@app.route('/processar_afd', methods=['POST'])
def processar_afd():
    estados = request.form['estados'].split(',')
    alfabeto = request.form['alfabeto'].split(',')
    transicoes = {}

    for estado in estados:
        for simbolo in alfabeto:
            chave_transicao = f'transicao_{estado}_{simbolo}'
            estado_destino = request.form.get(chave_transicao)
            if estado_destino:
                transicoes[(estado,simbolo)] = ' '.join(estado_destino.split(',')) #tirar a possibilidade de mais de um estado
            else:
                transicoes[(estado,simbolo)] = None

    inicial = request.form['inicial']
    finais = request.form['finais'].split(',')

    afd = autbase(estados, alfabeto, transicoes, inicial, [], finais, 'afd')
    print("Estados:", afd.estados)
    print("Alfabeto:", afd.alfabeto)
    print("Transições:", afd.transicoes)
    print("Estado Inicial:", afd.inicial)
    print("Estados Finais:", afd.finais)
    print("Tipo de Autômato:", afd.tipo_aut)
    

    caminho = desenha.desenha_automato(afd)
    relativo = os.path.relpath(caminho, 'static').replace("\\", "/")  # obtém o caminho relativo a 'static' com barras normais


    nomearquivo = request.form['nome']
    nomearquivo = nomearquivo + ".pkl"
    print(nomearquivo)
    os.makedirs('afds', exist_ok = True) 
    caminho = os.path.join('afds', nomearquivo) #cria o caminho para onde o arquivo deve ir, e define o nome do arquivo como aut+aleatorio
    with open(caminho, 'wb') as f:
        pickle.dump(afd, f)
    return redirect(url_for('mostrar_imagem', caminho=relativo))

@app.route('/processar_afn', methods=['POST'])
def processar_afn():
    estados = request.form['estados'].split(',')
    alfabeto = request.form['alfabeto'].split(',')
    transicoes = {}

    for estado in estados:
        for simbolo in alfabeto:
            chave_transicao = f'transicao_{estado}_{simbolo}'
            estado_destino = request.form.get(chave_transicao)
            if estado_destino:
                transicoes[(estado,simbolo)] = estado_destino.split(',')
            else:
                transicoes[(estado,simbolo)] = None

    inicial = request.form['inicial']
    finais = request.form['finais'].split(',')

    afn = autbase(estados, alfabeto, transicoes, inicial, [], finais, 'afn')
    print("Estados:", afn.estados)
    print("Alfabeto:", afn.alfabeto)
    print("Transições:", afn.transicoes)
    print("Estado Inicial:", afn.inicial)
    print("Estados Finais:", afn.finais)
    print("Tipo de Autômato:", afn.tipo_aut)


    nomearquivo = request.form['nome']
    nomearquivo = nomearquivo + ".pkl"
    print(nomearquivo)
    os.makedirs('afns', exist_ok = True) #confere se a pasta imagens existe
    caminho = os.path.join('afns', nomearquivo) #cria o caminho para onde o arquivo deve ir, e define o nome do arquivo como aut+aleatorio
    with open(caminho, 'wb') as f:
        pickle.dump(afn, f)

    caminho = desenha.desenha_automato(afn)
    relativo = os.path.relpath(caminho, 'static').replace("\\", "/")  # obtém o caminho relativo a 'static' com barras normais
    
    return redirect(url_for('mostrar_imagem', caminho=relativo))

@app.route('/mostrar_imagem')
def mostrar_imagem():
    caminho = request.args.get('caminho')
    imagem_url = url_for('static', filename=caminho)
    imagem_url = imagem_url.replace("\\", "/")
    imagem_url = os.path.join('/', f"{imagem_url}.png")
    return render_template('imagem.html', caminho=imagem_url)

@app.route('/mostrar_validade')
def mostrar_validade():
    caminho = request.args.get('caminho')
    resultado = request.args.get('resultado')
    imagem_url = url_for('static', filename=caminho)
    imagem_url = imagem_url.replace("\\", "/")
    imagem_url = os.path.join('/', f"{imagem_url}.png")
    return render_template('mostrar_validade.html', caminho=imagem_url , resultado=resultado)

@app.route('/mostrar_equivalencia')
def mostrar_equivalencia():
    caminho1 = request.args.get('caminho1')
    caminho2 = request.args.get('caminho2')
    resultado = request.args.get('resultado')
    imagem_url1 = url_for('static', filename=caminho1)
    imagem_url1 = imagem_url1.replace("\\", "/")
    imagem_url1 = os.path.join('/', f"{imagem_url1}.png")
    imagem_url2 = url_for('static', filename=caminho2)
    imagem_url2= imagem_url2.replace("\\", "/")
    imagem_url2 = os.path.join('/', f"{imagem_url2}.png")
    return render_template('mostrar_equivalencia.html', caminho1=imagem_url1, caminho2=imagem_url2 , resultado=resultado)

@app.route('/processarconverter', methods=['POST'])
def conversao():
    arquivo = request.form['arquivo']
    caminho = os.path.join('afns', arquivo)
    
    caminho = caminho.replace("\\", "/")
    print(caminho)

    
    with open(caminho, 'rb') as f:
        afn = pickle.load(f)
         
        
    print(afn.estados)
    print(afn.alfabeto)
    print(afn.transicoes)
    print(afn.inicial)
    print(afn.finais)

    convertido = converte.afn_to_afd(afn)

    nomearquivo = request.form['arquivo']
    nomearquivo = nomearquivo.replace(".pkl", "convertido")

    nomearquivo = nomearquivo + ".pkl"
    print(nomearquivo)
    os.makedirs('afds', exist_ok = True) #confere se a pasta imagens existe
    caminho = os.path.join('afds', nomearquivo) #cria o caminho para onde o arquivo deve ir, e define o nome do arquivo como aut+aleatorio
    with open(caminho, 'wb') as f:
        pickle.dump(convertido, f)

    caminho = desenha.desenha_automato(convertido)
    relativo = os.path.relpath(caminho, 'static').replace("\\", "/")  # obtém o caminho relativo a 'static' com barras normais
    
    return redirect(url_for('mostrar_imagem', caminho=relativo))

@app.route('/processarminimizar', methods=['POST'])
def mini():
    arquivo = request.form['arquivo']
    caminho = os.path.join('afds', arquivo)
    
    caminho = caminho.replace("\\", "/")
    print(caminho)

    
    with open(caminho, 'rb') as f:
        afd = pickle.load(f)
         
        
    print(afd.estados)
    print(afd.alfabeto)
    print(afd.transicoes)
    print(afd.inicial)
    print(afd.finais)

    min = minimiza.minimizacao(afd)

    nomearquivo = request.form['arquivo']
    nomearquivo = nomearquivo.replace(".pkl", "minimizado")

    nomearquivo = nomearquivo + ".pkl"
    print(nomearquivo)
    os.makedirs('afds', exist_ok = True) #confere se a pasta imagens existe
    caminho = os.path.join('afds', nomearquivo) #cria o caminho para onde o arquivo deve ir, e define o nome do arquivo como aut+aleatorio
    with open(caminho, 'wb') as f:
        pickle.dump(min, f)

    caminho = desenha.desenha_automato(min)
    relativo = os.path.relpath(caminho, 'static').replace("\\", "/")  # obtém o caminho relativo a 'static' com barras normais
    
    return redirect(url_for('mostrar_imagem', caminho=relativo))


@app.route('/geraimagem', methods=['POST'])
def image():
    arquivo = request.form['arquivo']
    print(arquivo)
    diretorio, arquivof = arquivo.rsplit('/', 1)
    caminho = os.path.join(diretorio, arquivof)
    
    caminho = caminho.replace("\\", "/")
    print(caminho)

    
    with open(caminho, 'rb') as f:
        aut = pickle.load(f)
         
        
    print(aut.estados)
    print(aut.alfabeto)
    print(aut.transicoes)
    print(aut.inicial)
    print(aut.finais)


    caminho = desenha.desenha_automato(aut)
    relativo = os.path.relpath(caminho, 'static').replace("\\", "/")  # obtém o caminho relativo a 'static' com barras normais
    
    return redirect(url_for('mostrar_imagem', caminho=relativo))

@app.route('/verifica', methods=['POST'])
def verifica():
    arquivo = request.form['arquivo']
    palavra = request.form['palavra'].split(',')

    diretorio, arquivof = arquivo.rsplit('/', 1)
    caminho = os.path.join(diretorio, arquivof)
    
    caminho = caminho.replace("\\", "/")

    
    with open(caminho, 'rb') as f:
        aut = pickle.load(f)

    caminho = desenha.desenha_automato(aut)
    relativo = os.path.relpath(caminho, 'static').replace("\\", "/")  # obtém o caminho relativo a 'static' com barras normais
    
    verpalavra = verificar_validade.verifica_aceita(aut, palavra)

    quandoverdade = f"A palavra {palavra}  é aceita pelo automato"
    quandonverdade = f"A palavra {palavra} não é aceita pelo automato"

    if verpalavra == 1:
        return redirect(url_for('mostrar_validade', caminho=relativo, resultado=quandoverdade))
    else:
        return redirect(url_for('mostrar_validade', caminho=relativo, resultado=quandonverdade))

@app.route('/processaequivalencia', methods=['POST'])
def pequivale():
    arquivo1 = request.form['arquivo1']
    arquivo2 = request.form['arquivo2']

    #caminho do arquivo 1

    diretorioa1, arquivoa1 = arquivo1.rsplit('/', 1)
    caminhoa1 = os.path.join(diretorioa1, arquivoa1)
    
    caminhoa1 = caminhoa1.replace("\\", "/")

    #caminho do arquivo 2

    diretorioa2, arquivoa2 = arquivo2.rsplit('/', 1)
    caminhoa2 = os.path.join(diretorioa2, arquivoa2)
    
    caminhoa2 = caminhoa2.replace("\\", "/")
    
    #abre os arquivos
    
    with open(caminhoa1, 'rb') as f:
        aut1 = pickle.load(f)

    with open(caminhoa2, 'rb') as f:
        aut2 = pickle.load(f)

    #imagem dos automatos

    caminho1 = desenha.desenha_automato(aut1)
    relativo1 = os.path.relpath(caminho1, 'static').replace("\\", "/")  # obtém o caminho relativo a 'static' com barras normais
    
    caminho2 = desenha.desenha_automato(aut2)
    relativo2 = os.path.relpath(caminho2, 'static').replace("\\", "/")  # obtém o caminho relativo a 'static' com barras normai

    #verifica se os automatos sao equivalentes
    result = equivalencia.equivalencia(aut1, aut2)


    quandoverdade = "Os automatos são equivalentes"
    quandonverdade = "Os automatos não são equivalentes"

    if result == True:
        return redirect(url_for('mostrar_equivalencia', caminho1=relativo1, caminho2=relativo2, resultado=quandoverdade))
    else:
        return redirect(url_for('mostrar_equivalencia', caminho1=relativo1, caminho2=relativo2, resultado=quandonverdade))

@app.route('/turing', methods=['POST'])
def processaturing():
    fita = request.form['fita'].replace(',', '')
    simbolosextras = request.form['simbolos_extras'].split(',')
    estados = request.form['estados'].split(',')
    inicial = request.form['inicial']
    estados_aceitacao = set(request.form['finais'].split(','))
    transicoes = {}

    for estado in estados:
        for simbolo in fita:
            chave_transicao = f'transicao_{estado}_{simbolo}'
            transicao_valor = request.form.get(chave_transicao)
            if transicao_valor:
                if transicao_valor != '-':
                    estado_destino, simbolo_escrever, direcao = transicao_valor.split(',')
                    transicoes[(estado, simbolo)] = (estado_destino, simbolo_escrever, direcao)
    
    if(simbolosextras):
        for estado in estados:
            for simbolo in simbolosextras:
                chave_transicao = f'transicao_{estado}_{simbolo}'
                transicao_valor = request.form.get(chave_transicao)
                if transicao_valor:
                    if transicao_valor != '-':
                        estado_destino, simbolo_escrever, direcao = transicao_valor.split(',')
                        transicoes[(estado, simbolo)] = (estado_destino, simbolo_escrever, direcao)  

    t = TuringMachine(fita, 
                  inicial=inicial,
                  final=estados_aceitacao,
                  transicoes=transicoes)

    res = t.executa()

    return render_template('resulturing.html', resultado=res)        

    

if __name__ == '__main__':
    app.run(debug=True)
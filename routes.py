import automato
import desenha
import os
import pickle
from flask import Flask, render_template, request,redirect, url_for

app = Flask(__name__, static_url_path='/static')

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

@app.route('/converter', methods=['GET'])
def converter():
    diretorio = 'afns'
    afns = lista_arquivos(diretorio)
    return render_template('converter.html', arquivos = afns)

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

    afd = automato.autbase(estados, alfabeto, transicoes, inicial, [], finais, 'afd')
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
    os.makedirs('afds', exist_ok = True) #confere se a pasta imagens existe
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

    afn = automato.autbase(estados, alfabeto, transicoes, inicial, [], finais, 'afn')
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
        pickle.dump(afd, f)

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

if __name__ == '__main__':
    app.run(debug=True)
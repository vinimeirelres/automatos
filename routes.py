import automato
import desenha
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/afd', methods=['GET'])
def afd():
    return render_template('afd.html')

@app.route('/afn', methods=['GET'])
def afn():
    return render_template('afn.html')

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


    desenha.desenha_automato(afd)

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


    desenha.desenha_automato(afn)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request

app = Flask(__name__)


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

       
@app.route('/')
def ola():
    return "<h1>Ola</h1>"


@app.route('/jogos')
def jogos():
    jogo1 = Jogo('Super Mario', 'Acao', 'SNES')
    jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
    lista = [jogo1, jogo2]
    return render_template('index.html', titulo = 'Teste', jogos = lista)

@app.route('/jogos/novo')
def novo():
    return render_template('/jogos/novo.html')

@app.route('/jogos/criar')
def criar():
    nome = request.form['nome']
    categorua = request.form['categoria']
    console = request.form['console']
    
app.run()

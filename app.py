from flask import Flask, render_template
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('login.html')

@app.route('/autenticar', methods = ['GET'])
def autenticar():
    nome = request.args.get('nome')
    curso = request.args.get('curso')
    cidade = request.args.get('cidade')
    return render_template(
        'autenticar.html',
        nome=nome,
        curso=curso,
        cidade=cidade
    )

if __name__ == '__main__':
    app.run(debug=True)
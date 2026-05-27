from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/recebedados', methods = ['POST'])
def recebedados():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    estado = request.form['estado']
    formacao = request.form['formacao']
    modalidade = request.form.getlist('modalidade')

    if senha == 12345:
        return f"Senha correta!"
    else:
        return f"Senha incorreta!"

    return "Olá {}({}), vi que você é do {}, sua formação é {} e tem interesse na modalidade {}".format(nome, email, estado, formacao, modalidade)

if __name__ == '__main__':
    app.run(debug=True)
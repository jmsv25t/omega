# app.py

from flask import Flask, render_template, request, redirect, url_for

# 1. Inicializa o aplicativo Flask
app = Flask(__name__)

# Rotas de Acesso
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # SIMULAÇÃO DE SUCESSO DE LOGIN -> REDIRECIONA PARA O DASHBOARD
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        # SIMULAÇÃO DE SUCESSO DE CADASTRO -> REDIRECIONA PARA O DASHBOARD
        return redirect(url_for('dashboard'))
    return render_template('cadastro.html')

# Rotas Pós-Login
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/funcionarios')
def funcionarios():
    return render_template('funcionarios.html')

# NOVAS ROTAS ESSENCIAIS
@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

@app.route('/agendar')
def agendar():
    return render_template('agendar.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html')

if __name__ == '__main__':
    # Rodar o servidor em modo de desenvolvimento
    app.run(debug=True)

# app.py

from flask import Flask, render_template, request, redirect, url_for

# 1. Inicializa o aplicativo Flask
app = Flask(__name__)

# 2. Rota para a tela de Pré-Cadastro/Login
@app.route('/')
def index():
    # Renderiza o arquivo HTML que contém a tela inicial
    return render_template('index.html')

# 3. Rota para a tela de Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Esta parte é um MOCK (simulação) de como o login funcionaria
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        # Em um sistema real, você verificaria o email/senha no banco de dados.
        print(f"Tentativa de Login: {email}")
        
        # Redireciona para o Dashboard após o login (simulação de sucesso)
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

# 4. Rota para a tela de Cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        # Esta parte é um MOCK (simulação) de como o cadastro funcionaria
        dados = request.form
        
        # Em um sistema real, você salvaria os dados no banco de dados.
        print(f"Novo Cadastro: {dados.get('nome')} - Tipo: {dados.get('tipo_conta')}")
        
        # Redireciona para o Dashboard após o cadastro (simulação de sucesso)
        return redirect(url_for('dashboard'))
        
    return render_template('cadastro.html')

# 5. Rota para a tela Pós-Login (Dashboard/Salões)
@app.route('/dashboard')
def dashboard():
    # Esta é a tela que lista os salões
    return render_template('dashboard.html')

# 6. Rota para a tela de Funcionários
@app.route('/funcionarios')
def funcionarios():
    # Esta é a tela que lista os funcionários e suas agendas
    return render_template('funcionarios.html')

# 7. Executa o servidor
if __name__ == '__main__':
    # 'debug=True' é útil para desenvolvimento
    app.run(debug=True)

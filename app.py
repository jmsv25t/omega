from flask import Flask, render_template, request, redirect, url_for

# 1. Inicializa o aplicativo Flask
app = Flask(__name__)

# --- ROTAS DE ACESSO E AUTENTICAÇÃO ---

# Rota principal (Tela de Pré-Cadastro/Login)
@app.route('/')
def index():
    """Renderiza a tela inicial."""
    return render_template('index.html')

# Rota de Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Processa o login do usuário."""
    if request.method == 'POST':
        # Em um sistema real, você verificaria o email/senha no banco de dados.
        email = request.form.get('email')
        print(f"Tentativa de Login: {email}")
        
        # Simulação de sucesso: redireciona para o Dashboard
        return redirect(url_for('dashboard'))
        
    return render_template('login.html')

# Rota de Cadastro
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    """Processa o cadastro de novos usuários."""
    if request.method == 'POST':
        # Em um sistema real, você salvaria os dados no banco de dados.
        dados = request.form
        print(f"Novo Cadastro: {dados.get('nome')} - Tipo: {dados.get('tipo_conta')}")
        
        # Simulação de sucesso: redireciona para o Dashboard
        return redirect(url_for('dashboard'))
        
    return render_template('cadastro.html')

# Rota de Recuperação de Senha
@app.route('/recuperar', methods=['GET', 'POST'])
def recuperar_senha():
    """Exibe e processa o formulário de recuperação de senha."""
    if request.method == 'POST':
        email = request.form.get('email')
        print(f"Solicitação de recuperação de senha para: {email}")
        
        # Simulação de sucesso: redireciona para a tela de aviso
        return redirect(url_for('aviso_recuperacao'))
        
    return render_template('recuperar_senha.html')

# Rota de Aviso após Solicitação de Recuperação
@app.route('/aviso-recuperacao')
def aviso_recuperacao():
    """Informa ao usuário que o link de recuperação foi enviado."""
    return render_template('aviso_recuperacao.html')

# --- ROTAS PÓS-LOGIN ---

# Rota do Dashboard (Listagem de Salões)
@app.route('/dashboard')
def dashboard():
    """Tela inicial após login/cadastro, listando os salões."""
    return render_template('dashboard.html')

# Rota de Detalhes dos Funcionários e Agenda
@app.route('/funcionarios')
def funcionarios():
    """Detalhes de serviços e agenda dos funcionários."""
    return render_template('funcionarios.html')

# Rota de Lista de Serviços
@app.route('/servicos')
def servicos():
    """Lista de serviços e preços oferecidos."""
    return render_template('servicos.html')

# Rota de Agendamento
@app.route('/agendar')
def agendar():
    """Formulário para selecionar serviço, profissional e horário."""
    return render_template('agendar.html')

# Rota de Perfil do Usuário
@app.route('/perfil')
def perfil():
    """Visualização de dados pessoais e agendamentos futuros do usuário."""
    return render_template('perfil.html')

# --- EXECUÇÃO ---

if __name__ == '__main__':
    # Roda o servidor. 'debug=True' é útil durante o desenvolvimento.
    app.run(debug=True)

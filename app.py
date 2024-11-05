from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de Usuário
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# Cria o banco de dados
with app.app_context():
    db.create_all()

# Rota para a página de cadastro
@app.route('/user_registration', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        new_user = User(name=name, email=email)
        
        # Adiciona e salva o novo usuário
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('registered_users'))
        except:
            return "Houve um problema ao adicionar o usuário."
    else:
        return render_template('register.html')

# Rota para exibir os usuários cadastrados
@app.route('/registered_users')
def usuarios():
    users = User.query.all()
    return render_template('users.html', users=users)

# Página inicial que redireciona para o cadastro
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contact_us')
def contato():
    return render_template("contact.html")

@app.route('/about_us')
def quemsomos():
    return render_template("aboutus.html")

@app.route('/payment_of_plans')
def pagamentos():
    return render_template("plans.html")

@app.route('/available_courses')
def cursos():
    return render_template("courses.html")

if __name__ == "__main__":
    app.run(debug=True)

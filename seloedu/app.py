from flask import Flask, render_template 

app = Flask(__name__)

users = [
    {"id": 1, "nome": "Lucas Silva",    "email": "lucas.silva@email.com", "perfil": "Coordenador", "status": "ativo"},
    {"id": 2, "nome": "Fernanda Souza", "email": "fernanda.souza@email.com", "perfil": "Supervisor", "status": "inativo"},
    {"id": 3, "nome": "Rafael Costa",   "email": "rafael.costa@email.com", "perfil": "Desenvolvedor", "status": "ativo"},
    {"id": 4, "nome": "Juliana Lima",   "email": "juliana.lima@email.com", "perfil": "Analista de Dados", "status": "inativo"},
    {"id": 5, "nome": "Bruno Alves",    "email": "bruno.alves@email.com", "perfil": "Designer", "status": "ativo"},
    {"id": 6, "nome": "Patricia Melo",  "email": "patricia.melo@email.com", "perfil": "QA", "status": "ativo"}
]


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("lauth/login.html")
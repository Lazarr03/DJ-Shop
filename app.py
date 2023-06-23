from flask import Flask, render_template, request
import sqlite3
from forms import RegistrationForm, LoginForm
from hashlib import sha256

app = Flask(__name__)
app.secret_key = "__privatekey__"


@app.route("/")
def home():
    return render_template("/base.html")


@app.route("/login")
def pageLogin():
    return render_template("/login.html")


# Prijava
@app.route("/Login", methods=["POST"])
def logovanje():
    name = request.form["userName"]
    sifra = request.form["passWord"]
    kodSifra = sifra.encode("utf-8")
    hesSifra = sha256(kodSifra).hexdigest()
    loginform = LoginForm()
    con = sqlite3.connect("users.db")
    c = con.cursor()
    statement = f"SELECT * from users WHERE username=? AND password=?;"
    c.execute(statement, (name, hesSifra))
    user = c.fetchone()
    if user:
        return render_template("/base.html")
    else:
        return render_template("/error.html")


@app.route("/register")
def pageRegister():
    return render_template("/register.html")


# Registracija
@app.route("/registrovanje", methods=["POST", "GET"])
def registrovanje():
    Registrationform = RegistrationForm()
    con = sqlite3.connect("users.db")
    c = con.cursor()
    if request.method == "POST":
        if request.form["username"] != "" and request.form["password"] != "":
            name = request.form["username"]
            passWord = request.form["password"]
            kodSifra = passWord.encode("utf-8")
            hesSifra = sha256(kodSifra).hexdigest()
            email = request.form["email"]
            statement = f"SELECT * from users WHERE username=? AND password=?;"
            c.execute(statement, (name, hesSifra))
            data = c.fetchone()
            if data:
                return render_template("/error.html")
            else:
                if not data:
                    c.execute(
                        "INSERT INTO users (username,email,password) VALUES (?,?,?)",
                        (name, email, hesSifra),
                    )
                    con.commit()
                    con.close()
                return render_template("/base.html")
    elif request.method == "GET":
        return render_template("/register.html", form=RegistrationForm)


def __init__(self):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("CREATE  TABLE users (username text,email text, password text)")
    conn.commit()


app.run("0.0.0.0")
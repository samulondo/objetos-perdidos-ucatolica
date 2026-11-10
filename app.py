from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory
from functools import wraps
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "clave-demo-cambiar-en-produccion")
app.config["SESSION_COOKIE_HTTPONLY"] = True
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

# Credenciales de demostración. Se pueden cambiar mediante variables de entorno.
DEMO_USER = os.environ.get("ADMIN_USER", "admin")
DEMO_PASSWORD = os.environ.get("ADMIN_PASSWORD", "admin123")


def requiere_login(func):
    @wraps(func)
    def envoltura(*args, **kwargs):
        if not session.get("autenticado"):
            return redirect(url_for("login"))
        return func(*args, **kwargs)
    return envoltura


@app.route("/", methods=["GET"])
@requiere_login
def inicio():
    # Se entrega el HTML original directamente, sin renderizarlo ni modificarlo.
    return send_from_directory(app.static_folder, "pagina_original.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("autenticado"):
        return redirect(url_for("inicio"))
    if request.method == "POST":
        usuario = request.form.get("username", "")
        clave = request.form.get("password", "")
        if usuario == DEMO_USER and clave == DEMO_PASSWORD:
            session["autenticado"] = True
            session["usuario"] = usuario
            return redirect(url_for("inicio"))
        flash("Usuario o contraseña incorrectos.", "error")
    return render_template("login.html")


@app.route("/terminos")
def terminos():
    return render_template("terminos.html")


@app.route("/recuperar")
def recuperar():
    return render_template("recuperar.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

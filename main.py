from flask import Flask,render_template,request
import db

app= Flask(__name__)


@app.route("/")
def index():
    return render_template("login.html")

@app.route("/clientes")
def ver_clientes():
    lista=db.ver_clientes()
    return render_template("cliente.html",lista=lista)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
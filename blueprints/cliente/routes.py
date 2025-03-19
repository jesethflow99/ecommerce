from flask import Blueprint,render_template
import db


cliente=Blueprint("cliente",__name__)

@cliente.route("/")
def ver_clientes():
    lista=db.ver_clientes()
    return render_template("cliente.html",lista=lista)


@cliente.route("/<int:id>")
def ver_cliente(id):
    lista=db.ver_cliente(id)
    return render_template("cliente.html",lista=lista)


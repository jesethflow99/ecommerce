from flask import Blueprint,render_template
from db import Cliente


cliente=Blueprint("cliente",__name__)

@cliente.route("/")
def ver_clientes():
    lista=Cliente.READ_ALL()
    return render_template("cliente.html",lista=lista)


@cliente.route("/<int:id>")
def ver_cliente(id):
    lista=Cliente.READ_ONE(id)
    return render_template("cliente.html",lista=lista)


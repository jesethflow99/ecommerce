from flask import Flask,render_template,request
import db
from blueprints.cliente.routes import cliente


app= Flask(__name__)


app.register_blueprint(cliente,url_prefix="/cliente")

@app.route("/")
def index():
    return render_template("login.html")



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",use_reloader=True)
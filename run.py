from flask import Flask,jsonify
import os

from Blueprints.membros import membros


app = Flask(__name__)
app.register_blueprint(membros)

@app.route("/", methods=["GET"])
def hello():
    data = {"Mensagem":"Bem vindo"}
    return jsonify(data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
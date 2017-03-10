from flask import Flask,jsonify

from Blueprints.membros import membros


app = Flask(__name__)
app.register_blueprint(membros)

@app.route("/", methods=["GET"])
def hello():
    data = {"Mensagem":"Bem vindo"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)